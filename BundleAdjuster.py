import csfm


class BundleAdjuster:

    def __init__(self):
        self._bundle = csfm.BundleAdjuster()

    def run(self):
        self._bundle.run()

    def add_perspective_camera(self, desc, focal, k1, k2, focal_prior, k1_prior, k2_prior, fix_cameras):
        self._bundle.add_perspective_camera(desc, focal, k1, k2, focal_prior, k1_prior, k2_prior, fix_cameras)

    def add_shot(self, shot, camera, r0, r1, r2, t0, t1, t2, g0, g1, g2, gps_dop, dummy=False):
        self._bundle.add_shot(shot, camera, r0, r1, r2, t0, t1, t2, g0, g1, g2, gps_dop, dummy)

    def add_point(self, track, x, y, z, dummy=False):
        self._bundle.add_point(track, x, y, z, dummy)

    def add_observation(self, shot, track, x, y):
        self._bundle.add_observation(shot, track, x, y)

    def set_loss_function(self, loss_function, loss_function_threshold):
        self._bundle.set_loss_function(loss_function, loss_function_threshold)

    def set_reprojection_error_sd(self, reprojection_error_sd):
        self._bundle.set_reprojection_error_sd(reprojection_error_sd)

    def set_internal_parameters_prior_sd(self, exif_focal_sd, radial_distorsion_k1_sd, radial_distorsion_k2_sd):
        self._bundle.set_internal_parameters_prior_sd(exif_focal_sd, radial_distorsion_k1_sd, radial_distorsion_k2_sd)

    def set_num_threads(self, threads):
        self._bundle.set_num_threads(threads)
    
    def set_max_num_iterations(self, iteration):
        self._bundle.set_max_num_iterations(iteration)

    def get_perspective_camera(self, desc):
        return self._bundle.get_perspective_camera(desc)
    
    def get_shot(self, shot):
        return self._bundle.get_shot(shot)

    def get_point(self, track):
        return self._bundle.get_point(track)

    def brief_report(self):
        return self._bundle.brief_report()

    def full_report(self):
        return self._bundle.full_report()

