import isaaclab.sim as sim_utils
from isaaclab.assets import ArticulationCfg
from isaaclab.actuators import ImplicitActuatorCfg
# from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR

MORPHOPALM5_CONFIG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"/home/stw/dex_hand/source/dex_hand/dex_hand/model/MP5_new.usda",
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,
            # solver_position_iteration_count=4,
            # solver_velocity_iteration_count=0,
            fix_root_link=True,
        )),
    init_state=ArticulationCfg.InitialStateCfg(
        # TODO: set the initial joint positions for the MorphoPalm5
        joint_pos={ 

            "left_crank_base_joint": 0.5234, # 30.0 left positive joint 

            "left_coupler_crank_joint": -0.2163, # -12.4 left negitive joint

            "right_crank_base_joint": -0.5234, # -30.0 right positive joint 

            # "right_coupler_crank_joint": 0.0, # right negitive joint 

            "coupler_joint": 0.5934, # 34.0 target joint - this is the joint that the robot will try to control to a target position

        },

        pos=(0.0, 0.0, 0.104),
        # pos=(0.0, 0.0, 0.1124),
        rot=( 0.28228, 0.27567, -0.63889, -0.66041),  
        # rot = (0.7071067811865476, 0.7071067811865475, 0, 0)

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

