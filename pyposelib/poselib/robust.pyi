from typing import Tuple, List, Union
import numpy
import pyposelib

def estimate_absolute_pose(
    points2D: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points3D: List[numpy.ndarray[numpy.float64[3, 1]]], 
    camera_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_generalized_absolute_pose(
    points2D: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points3D: List[numpy.ndarray[numpy.float64[3, 1]]], 
    camera_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_relative_pose(
    points2D_1: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points2D_2: List[numpy.ndarray[numpy.float64[2, 1]]], 
    camera1_dict: Union[pyposelib.Camera, dict], 
    camera2_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_shared_focal_relative_pose(
    points2D_1: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points2D_2: List[numpy.ndarray[numpy.float64[2, 1]]], 
    camera1_dict: Union[pyposelib.Camera, dict], 
    camera2_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_fundamental(
    points2D_1: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points2D_2: List[numpy.ndarray[numpy.float64[2, 1]]], 
    camera1_dict: Union[pyposelib.Camera, dict], 
    camera2_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_homography(
    points2D_1: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points2D_2: List[numpy.ndarray[numpy.float64[2, 1]]], 
    camera1_dict: Union[pyposelib.Camera, dict], 
    camera2_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...

def estimate_generalized_relative_pose(
    points2D_1: List[numpy.ndarray[numpy.float64[2, 1]]], 
    points2D_2: List[numpy.ndarray[numpy.float64[2, 1]]], 
    camera1_dict: Union[pyposelib.Camera, dict], 
    camera2_dict: Union[pyposelib.Camera, dict], 
    ransac_opt: pyposelib.RansacOptions = pyposelib.RansacOptions(), 
    bundle_opt: pyposelib.BundleOptions = pyposelib.BundleOptions()) -> Tuple[pyposelib.CameraPose, dict]:...