# svh_grasp

Connecting Svh_hand with Ros and other sensors during grasp tasks.

## Launch

### Step 1: Start Schunk SVH Hand

```bash
source devel_isolated/setup.bash
roslaunch schunk_svh_driver svh_controller.launch
# debug launch
# roslaunch schunk_svh_driver svh_controller.launch standalone:=true
# roslaunch schunk_svh_driver svh_controller.launch standalone:=true simulation:=true gui:=true
```

### Step2: Start FSR force sensor

```bash
roslaunch svh_grasp adc_receiver.launch
```

### Step3: Start Leap Motion Control

```bash
roslaunch svh_grasp leap_interface.launch
```

### Final Step: Recording

```bash
rosbag record -O xxx.bag adc0_chatter adc1_chatter svh_controller/channel_currents svh_controller/channel_feedback svh_controller/channel_targets
```
