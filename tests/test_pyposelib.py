import pyposelib
import numpy as np
import pytest

def test_camera():
    pyposelib.Camera()
    pyposelib.Camera("PINHOLE", [1,1,0,0], 10, 10)
    #incorrect camera
    with pytest.raises(ValueError):
        pyposelib.Camera(np.random.randn(3,3), 10, 10)
    K = np.zeros((3,3))
    K[0,0] = 1
    K[1,1] = 1
    pyposelib.Camera(K, 10, 10)
    
def test_camera_pose():
    pyposelib.CameraPose(np.random.rand(4,1), np.random.rand(3,1))


def test_image():
    #TODO: binds for constructor with campose and cam not working yet
    pyposelib.Image()

def test_bundle_options():
    x = pyposelib.BundleOptions(max_iterations = 1337)
    assert x.max_iterations == 1337

def test_ransac_options():
    pyposelib.RansacOptions()

def test_relative_pose():
    pyposelib.estimate_relative_pose(np.random.randn(5,2), np.random.randn(5,2))

def test_fundamental():
    pyposelib.estimate_fundamental(np.random.randn(8,2), np.random.randn(8,2), {"real_focal_check": True})

def test_absolute_pose():
    camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}
    pyposelib.estimate_absolute_pose(np.random.randn(5,2), np.random.randn(5,3), camera)

def test_pnp():
    camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}
    pyposelib.pnp(np.random.randn(5,2), np.random.randn(5,3), camera)
    

def test_p3p():
    # note: probably should raise exception for n-points > 3
    pyposelib.p3p(np.random.randn(8,2), np.random.randn(8,3))
    
def test_batched_p3p():
    pyposelib.p3p(np.random.randn(10,3,2), np.random.randn(10,3,3))

def compare_p3p():
    N = 10_000
    x, y = np.random.randn(N,3,2), np.random.randn(N,3,3)
    poses = pyposelib.p3p(x,y)
    for i in range(N):
        pose = pyposelib.p3p(x[i],y[i])

def test_relative_pose():
    N = 10_000
    x, y = np.random.randn(N,2), np.random.randn(N,2)
    camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}
    pose = pyposelib.estimate_essential(x, y, camera, camera)
    cam = pyposelib.Camera("PINHOLE", [1,1,0,0], 10, 10)
    ransac_opts = pyposelib.RansacOptions()
    bundle_opts = pyposelib.BundleOptions()
    poses = pyposelib.estimate_essential(x, y, cam, cam, ransac_opts, bundle_opts)
    poses = pyposelib.estimate_essential(x, y, cam, ransac_opts, bundle_opts)


    
    
if __name__ == "__main__":
    #compare_p3p()
    test_relative_pose()
    print("All tests passed!")