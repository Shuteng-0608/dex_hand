import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
# from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

MORPHOPALM5_CONFIG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(usd_path=f"/home/stw/myAssets/MorphoPalm5.usd"),
    init_state=ArticulationCfg.InitialStateCfg(
        # TODO: set the initial joint positions for the MorphoPalm5
        joint_pos={ 

            "left_crank_base_joint": 29.99, # left positive joint

            "left_coupler_crank_joint": -12.395, # left negitive joint

            "right_crank_base_joint": -29.99, # right positive joint

            # "right_coupler_crank_joint": 0.0, # right negitive joint

            "coupler_joint": 34.0, # target joint - this is the joint that the robot will try to control to a target position

        },

        pos=(0.0, 0.0, 0.1),
        rot=( 0.28228, 0.27567, -0.63889, -0.66041),  

    ),
    actuators={

        "left_joint": ImplicitActuatorCfg(
            joint_names_expr=["left_crank_base_joint"], 
            damping=None, 
            stiffness=None),

        "right_joint": ImplicitActuatorCfg(
            joint_names_expr=["right_crank_base_joint"], 
            damping=None, 
            stiffness=None),

        },
)