# svh_grasp

Connecting Svh_hand with Ros and other sensors during grasp tasks.

## Launch

### Step 1: Start Schunk SVH Hand

```bash
source devel_isolated/setup.bash
roslaunch schunk_svh_driver svh_controller.launch
# debug launch
# roslaunch schunk_svh_driver svh_controller.launch standalone:=true
```

### Step2: Start FSR force sensor

```bash
roslaunch svh_grasp adc_receiver.launch
```
