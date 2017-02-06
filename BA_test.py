import json
import mydataset as md
from BundleAdjuster import BundleAdjuster


if __name__ == '__main__':
    with open('tracks.csv', 'r') as f:
        graph, data, track_data = md.load_tracks_graph(f)

    with open('reconstruction.json', 'r') as f:
        reconstruct = json.load(f)[0]

    ba = BundleAdjuster()


    for k,v in reconstruct['cameras'].items():
        pt = v.get('projection_type', 'perspective')
        ba.add_perspective_camera(str(k), v['focal'], v['k1'], v['k2'],
                                  v['focal_prior'], v.get('k1_prior', 0.0), v.get('k2_prior', 0.0), False)
    
    for k,v in reconstruct['shots'].items():
        r = v['rotation']
        t = v['translation']
        g = v['gps_position']
        ba.add_shot(str(k), str(v['camera']), r[0], r[1], r[2], t[0], t[1], t[2], g[0], g[1], g[2], v['gps_dop'], False)

    for k,v in reconstruct['points'].items():
        p = v['coordinates']
        ba.add_point(str(k), p[0], p[1], p[2], False)

    for shot in reconstruct['shots']:
        if shot in graph:
            for track in graph[shot]:
                if track in reconstruct['points']:
                    ba.add_observation(str(shot), str(track), *graph[shot][track]['feature'])

    ba.set_loss_function('SoftLOneLoss', 1)
    ba.set_reprojection_error_sd(0.004)
    ba.set_internal_parameters_prior_sd(0.01, 0.01, 0.01)
    ba.set_num_threads(4)
    ba.set_max_num_iterations(50)

    ba.run()
    print ba.brief_report()


    print 'FFFFFFFFFFFFFFFFFFFFFFF'
