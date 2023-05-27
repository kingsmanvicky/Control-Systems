#Importing required packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec  


#Time array
t0 = 0 #[sec]
dt = 0.04 #[sec]
t_end = 50 #[sec]
t = np.arange(t0,t_end+dt,dt)


#Volume Parameters:
Vol_final = 100
dVol = 10


#Proportional Constants and water properties
Kp1 = 1000
Kp2 = 1000
Kp3 = 5000
density_water = 1000 #[kg/m^3]


#Initial Volumes for the respective tanks and Volume array
#Tank-1
vol_o1_i=30 
vol_r1_i=70 
vol_r1 = np.zeros(len(t))
vol_r1[0] = vol_r1_i
volume_Tank1 = np.zeros(len(t))
volume_Tank1[0] = vol_o1_i
error1 = np.zeros(len(t))
m_dot1 = Kp1*error1


#Tank-2:
vol_o2_i=40 
vol_r2_i=10
vol_r2 = np.zeros(len(t))
vol_r2[0] = vol_r2_i
volume_Tank2= np.zeros(len(t))
volume_Tank2[0] = vol_o2_i
error2 = np.zeros(len(t))
m_dot2 = Kp2*error2


#Tank-3: 
vol_o3_i=50
vol_r3_i=20
vol_r3 = vol_r3=vol_o3_i+1*t*np.sin(2*np.pi*(0.005*t)*t)
vol_r3[0] = vol_r3_i
volume_Tank3 = np.zeros(len(t))
volume_Tank3[0] = vol_o3_i
error3 = np.zeros(len(t))
m_dot3 = Kp3*error3

#Generating the rest of the array elements for the data to generate plot animation
for i in range(1,len(t)): 
    if i<300:
        vol_r1[i]=vol_r1_i
        vol_r2[i]=vol_r2_i+3*t[i]
    elif i<600:
        vol_r1[i]=20
        vol_r2[i]=vol_r2_i+3*t[i]
        time_temp2=t[i]
        temp2=vol_r2[i]
    elif i<900:
        vol_r1[i]=90
        vol_r2[i]=temp2-1*(t[i]-time_temp2)
    else:
        vol_r1[i]=50
        vol_r2[i]=temp2-1*(t[i]-time_temp2)


    error1[i-1]=vol_r1[i-1]-volume_Tank1[i-1]
    error2[i-1]=vol_r2[i-1]-volume_Tank2[i-1]
    error3[i-1]=vol_r3[i-1]-volume_Tank3[i-1]


    m_dot1[i]=Kp1*error1[i-1]
    m_dot2[i]=Kp2*error2[i-1]
    m_dot3[i]=Kp3*error3[i-1]


    volume_Tank1[i]=volume_Tank1[i-1]+(m_dot1[i-1]+m_dot1[i])/(2*density_water)*(dt)
    volume_Tank2[i]=volume_Tank2[i-1]+(m_dot2[i-1]+m_dot2[i])/(2*density_water)*(dt)
    volume_Tank3[i]=volume_Tank3[i-1]+(m_dot3[i-1]+m_dot3[i])/(2*density_water)*(dt)


vol_r1_2=vol_r1
vol_r2_2=vol_r2
vol_r3_2=vol_r3


def update_plot(num):
    if num>=len(volume_Tank1):
        num=len(volume_Tank1)-1

    tank_12.set_data([0,0],[-145,volume_Tank1[num]-110])
    tnk_1.set_data(t[0:num],volume_Tank1[0:num])
    vol_r1.set_data([-radius*width_ratio,radius*width_ratio],[vol_r1_2[num],vol_r1_2[num]])
    vol_r1_line.set_data([t0,t_end],[vol_r1_2[num],vol_r1_2[num]])

    tank_22.set_data([0,0],[-145,volume_Tank2[num]-110])
    tnk_2.set_data(t[0:num],volume_Tank2[0:num])
    vol_r2.set_data([-radius*width_ratio,radius*width_ratio],[vol_r2_2[num],vol_r2_2[num]])
    vol_r2_line.set_data([t0,t_end],[vol_r2_2[num],vol_r2_2[num]])

    tank_32.set_data([0,0],[-145,volume_Tank3[num]-110])
    tnk_3.set_data(t[0:num],volume_Tank3[0:num])
    vol_r3.set_data([-radius*width_ratio,radius*width_ratio],[vol_r3_2[num],vol_r3_2[num]])
    vol_r3_line.set_data([t0,t_end],[vol_r3_2[num],vol_r3_2[num]])


    return  vol_r1,tank_12,vol_r1_line,tnk_1,vol_r2,tank_22,vol_r2_line,tnk_2,vol_r3,tank_32,vol_r3_line,tnk_3

##################### ANIMATION #####################
frame_amount = len(t)
width_ratio = 1 
radius = 5 #[m]
final_volume = 100 #[m^3]
bottom = 0 #[m^3]


fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,3)

# Create object for Tank1
ax0=fig.add_subplot(gs[0,0],facecolor=(0.9,0.9,0.9))
vol_r1,=ax0.plot([],[],'r',linewidth=2)
tank_12,=ax0.plot([],[],'royalblue',linewidth=500,zorder=0)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(bottom,final_volume)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(bottom,final_volume+dVol,dVol))
plt.ylabel('tank volume [m^3]')
plt.title('Tank 1')

# Create object for Tank2
ax1=fig.add_subplot(gs[0,1],facecolor=(0.9,0.9,0.9))
vol_r2,=ax1.plot([],[],'r',linewidth=2)
tank_22,=ax1.plot([],[],'royalblue',linewidth=500,zorder=0)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(bottom,final_volume)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(bottom,final_volume+dVol,dVol))
plt.title('Tank 2')


# Create object for Tank3
ax2=fig.add_subplot(gs[0,2],facecolor=(0.9,0.9,0.9))
vol_r3,=ax2.plot([],[],'r',linewidth=2)
tank_32,=ax2.plot([],[],'royalblue',linewidth=500,zorder=0)
plt.xlim(-radius*width_ratio,radius*width_ratio)
plt.ylim(bottom,final_volume)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(bottom,final_volume+dVol,dVol))
plt.title('Tank 3')

# Create volume function
ax3=fig.add_subplot(gs[1,:], facecolor=(0.9,0.9,0.9))
vol_r1_line,=ax3.plot([],[],'r',linewidth=2)
vol_r2_line,=ax3.plot([],[],'r',linewidth=2)
vol_r3_line,=ax3.plot([],[],'r',linewidth=2)
tnk_1,=ax3.plot([],[],'blue',linewidth=4,label='Tank 1')
tnk_2,=ax3.plot([],[],'green',linewidth=4,label='Tank 2')
tnk_3,=ax3.plot([],[],'red',linewidth=4,label='Tank 3')
plt.xlim(0,t_end)
plt.ylim(0,final_volume)
plt.ylabel('tank volume [m^3]')
plt.grid(True)
plt.legend(loc='upper right',fontsize='small')

plane_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()