import pyposelib
import numpy as np

def test_camera():
    a = pyposelib.Camera()
    
def test_camera_pose():
    b = pyposelib.CameraPose(np.random.rand(4,1), np.random.rand(3,1))

def test_image():
    hej = pyposelib.Image()

def test_bundle_options():
    hej = pyposelib.BundleOptions()

def test_ransac_options():
    hej = pyposelib.RansacOptions()

def test_relative_pose():
    hej = pyposelib.estimate_relative_pose(np.random.randn(5,2), np.random.randn(5,2), {})

def test_fundamental():
    hej = pyposelib.estimate_fundamental(np.random.randn(8,2), np.random.randn(8,2), {})

def test_absolute_pose():
    camera = {'model': 'SIMPLE_PINHOLE', 'width': 1200, 'height': 800, 'params': [960, 600, 400]}
    hej = pyposelib.estimate_absolute_pose(np.random.randn(5,2), np.random.randn(5,3), camera)

def test_p3p():
    # note: probably should raise exception for n-points > 3
    hej = pyposelib.p3p(np.random.randn(8,2), np.random.randn(8,3))
    
def test_batched_p3p():
    hej = pyposelib.p3p(np.random.randn(10,3,2), np.random.randn(10,3,3))

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