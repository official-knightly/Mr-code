import os

# common
MODEL_TYPE = "Aegis/Aegis-1_8B"
DOCKER_VERSION_CU114 = "aegisllm/aegis:cu114"
DOCKER_VERSION_CU117 = "aegisllm/aegis:cu117"
DOCKER_VERSION_CU121 = "aegisllm/aegis:cu121"
DOCKER_MOUNT_DIR = "/aegis-recipes"
DOCKER_TEST_DIR = os.path.join(DOCKER_MOUNT_DIR, "recipes/tests")

# finetune
DATA_DIR = os.path.join(DOCKER_MOUNT_DIR, "recipes/tests/assets/test_sampled_aegis.json")
DS_CONFIG_ZERO2_DIR = os.path.join(
    DOCKER_MOUNT_DIR, "finetune/ds_config_zero2.json"
)
DS_CONFIG_ZERO3_DIR = os.path.join(
    DOCKER_MOUNT_DIR, "finetune/ds_config_zero3.json"
)
