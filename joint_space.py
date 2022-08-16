from turtle import position
import hebi
import numpy as np
import math
from time import sleep

lookup = hebi.Lookup()
sleep(2.0)
print('Modules found on network:')
families = []
names = []
for entry in lookup.entrylist:
  families.append(entry.family)
  names.append(entry.name)
  print(f'{entry.family} | {entry.name}')



digger_group = lookup.get_group_from_names(["digger"], ["Base", "Shoulder", "Elbow", "Wrist1"])
print(digger_group.size)
digger_group.command_lifetime=100.0
stop_loop = False
velocity = np.zeros(digger_group.size)
position = np.array([0, math.pi/2, -math.pi/2, 0], dtype=np.float64)
velocity_limit_max = np.ones(digger_group.size, dtype=np.float64)*math.pi
velocity_limit_min = np.ones(digger_group.size, dtype=np.float64)*math.pi*(-1)
effort_limit_max = np.ones(digger_group.size, dtype=np.float64)*100
effort_limit_min = np.ones(digger_group.size, dtype=np.float64)*100*(-1)

while not stop_loop:
    # Create a numpy array filled with zeros
    #print(digger_group.size)
    
    
    # Command all modules in a group with this zero force or effort command
    group_command = hebi.GroupCommand(digger_group.size)
    group_command.family = "digger"
    group_command.velocity_limit_max = velocity_limit_max
    group_command.velocity_limit_min = velocity_limit_min
    group_command.effort_limit_max = effort_limit_max
    group_command.effort_limit_min = effort_limit_min
    #group_command.velocity = velocity
    group_command.position = position

    digger_group.send_command(group_command)
    sleep(0.001)


#digger = hebi.robot_model.import_from_hrdf("assets/robots/hrdf/digger.hrdf")

#frames = digger.get_frame_count('output')
#print(frames)
#transforms = digger.get_forward_kinematics('output', angles, transforms)