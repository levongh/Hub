import pytest
from hub import Dataset


enabled_datasets = pytest.mark.parametrize(
    "ds",
    ["memory_ds", "local_ds", "s3_ds", "hub_cloud_ds"],  # TODO: add hub cloud
    indirect=True,
)

enabled_persistent_dataset_generators = pytest.mark.parametrize(
    "ds_generator",
    ["local_ds_generator", "s3_ds_generator", "hub_cloud_ds_generator"],
    indirect=True,
)


@pytest.fixture
def memory_ds(memory_path):
    return Dataset(memory_path)


@pytest.fixture
def local_ds(local_ds_generator):
    return local_ds_generator()


@pytest.fixture
def local_ds_generator(local_path):
    def generate_local_ds():
        return Dataset(local_path)

    return generate_local_ds


@pytest.fixture
def s3_ds(s3_ds_generator):
    return s3_ds_generator()


@pytest.fixture
def s3_ds_generator(s3_path):
    def generate_s3_ds():
        return Dataset(s3_path)

    return generate_s3_ds


@pytest.fixture
def hub_cloud_ds(hub_cloud_ds_generator):
    return hub_cloud_ds_generator()


@pytest.fixture
def hub_cloud_ds_generator(hub_cloud_path, hub_cloud_dev_token):
    def generate_hub_cloud_ds():
        return Dataset(hub_cloud_path, token=hub_cloud_dev_token)

    return generate_hub_cloud_ds


@pytest.fixture
def ds(request):
    """Used with parametrize to use all enabled dataset fixtures."""
    return request.getfixturevalue(request.param)


@pytest.fixture
def ds_generator(request):
    """Used with parametrize to use all enabled persistent dataset generator fixtures."""
    return request.getfixturevalue(request.param)
