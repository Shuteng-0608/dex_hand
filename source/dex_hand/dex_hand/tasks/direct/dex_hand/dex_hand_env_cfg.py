# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from dex_hand.robots import MORPHOPALM5_CONFIG

from isaaclab.assets import ArticulationCfg
from isaaclab.envs import DirectRLEnvCfg
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass
from typing import List, Tuple, Dict
import math


@configclass
class DexHandEnvCfg(DirectRLEnvCfg):
    # env
    decimation = 2 # 
    episode_length_s = 10.0 # each episode lasts 5 seconds, maybe try 10s or longer later
    # - spaces definition
    action_space = 2 # 2个主动关节
    observation_space = 6 # 2个主动关节位置 + 2个主动关节速度 + 目标关节位置 + 目标关节速度
    state_space = 0

    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 480, render_interval=decimation)

    # robot(s)
    robot_cfg: ArticulationCfg = MORPHOPALM5_CONFIG.replace(prim_path="/World/envs/env_.*/Robot")

    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=1024, env_spacing=2.0, replicate_physics=True)

    # joints
    active_joints: List[str] = ["left_crank_base_joint", "right_crank_base_joint"]
    negitive_joints: List[str] = ["left_coupler_crank_joint"]
    target_joint: str = "coupler_joint"

    # ====================
    # Task Parameters
    # ====================

    target_joint_angle: float = -30.0 * math.pi / 180.0
    target_tolerance: float = 5.0 * math.pi / 180.0  
    target_angle_range: Tuple[float, float] = (
        target_joint_angle - target_tolerance,  
        target_joint_angle + target_tolerance  
    )

    # 关节限制
    joint_limits: Dict[str, Tuple[float, float]] = {
        "left_crank_base_joint": (
            -0.5 * math.pi, 
            0.5 * math.pi  
        ),
        "right_crank_base_joint": (
            -0.5 * math.pi,
            0.5 * math.pi 
        ),
        "left_coupler_crank_joint": (
            -0.5 * math.pi, 
            0.5 * math.pi   
        ),
        "coupler_joint": (
            -0.5 * math.pi, 
            0.5 * math.pi
        ), 
    }
    
    action_scale: float = 1.0
    
    # ====================
    # Reward Coefficients
    # ====================
    rew_scale_target_angle: float = 5.0     # 目标角度奖励
    rew_scale_milestone: float = 10.0       # 跨越分岔平面奖励
    rew_scale_energy: float = 0.01          # 能耗惩罚
    rew_scale_crossing_speed: float = 0.5   # 快速穿越奖励
    rew_scale_success: float = 100.0         # 成功奖励
   