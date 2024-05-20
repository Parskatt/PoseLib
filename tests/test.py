import pyposelib
import numpy as np
from time import perf_counter

def test_camera():
    a = pyposelib.Camera()
    assert a is not None
    
def test_camera_pose():
    b = pyposelib.CameraPose(np.random.rand(4,1), np.random.rand(3,1))
    assert b is not None

def test_image():
    hej = pyposelib.Image()
    assert hej is not None

def test_relative_pose():
    hej = pyposelib.estimate_relative_pose(np.random.randn(5,2), np.random.randn(5,2), {})
    assert hej is not None

def test_fundamental():
    hej = pyposelib.estimate_fundamental(np.random.randn(8,2), np.random.randn(8,2), {})
    assert hej is not None

def test_absolute_pose():
    hej = pyposelib.estimate_absolute_pose([np.random.randn(5,2)], [np.random.randn(5,3)], {})
    assert hej is not None

def test_p3p():
    # note: probably should raise exception for n-points > 3
    hej = pyposelib.p3p(np.random.randn(8,2), np.random.randn(8,3))
    assert hej is not None

def test_batched_p3p():
    hej = pyposelib.p3p(np.random.randn(10,3,2), np.random.randn(10,3,3))
    assert hej is not None

def compare_p3p():
    N = 100_000
    x, y = np.random.randn(N,3,2), np.random.randn(N,3,3)
    t0 = perf_counter()
    poses = pyposelib.p3p(x,y)
    t1 = perf_counter()
    print(f"Batched p3p: {t1-t0:.2f} s")
    t0 = perf_counter()
    #x,y = np.random.randn(3,2), np.random.randn(3,3)
    for i in range(N):
        pose = pyposelib.p3p(x[i],y[i])
    t1 = perf_counter()
    print(f"p3p: {t1-t0:.2f} s")

def test_relative_pose():
    N = 10_000
    x, y = np.random.randn(N,2), np.random.randn(N,2)
    t0 = perf_counter()
    camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}
    #x,y = np.random.randn(3,2), np.random.randn(3,3)
    pose = pyposelib.estimate_essential(x, y, camera, camera)
    t1 = perf_counter()
    print(f"relpose: {t1-t0:.2f} s")
    t0 = perf_counter()
    cam = pyposelib.Camera("PINHOLE", [1,1,0,0], 10, 10)
    ransac_opts = pyposelib.RansacOptions()
    bundle_opts = pyposelib.BundleOptions()
    poses = pyposelib.estimate_essential(x, y, cam, cam, ransac_opts, bundle_opts)
    t1 = perf_counter()
    print(f"Batched relpose: {t1-t0:.2f} s")
    poses = pyposelib.estimate_essential(x, y, cam, ransac_opts, bundle_opts)


    
    
if __name__ == "__main__":
    #compare_p3p()
    test_relative_pose()
    print("All tests passed!")