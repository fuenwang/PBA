def SplitModelByImage(graph, reconstruction, image, finish_images, frames=20):
#   image will be finish_images[-1]

    shots = sorted(reconstruction['shots'].keys())
    sub_model = {'cameras':{}, 'shots':{}, 'points':{}}
    
    sub_model['cameras'] = reconstruction['cameras'].copy()
    related_image = []
    for track in graph[image]:
        if track in reconstruction['points']:
            #sub_model['points'][track] = reconstruction['points'][track].copy()
            for img in graph[track]:
                if img in reconstruction['shots'] and img not in related_image:
                    related_image.append(img)
    print related_image
    for img in related_image:
        sub_model['shots'][img] = reconstruction['shots'][img].copy()
        for track in graph[img]:
            if track in reconstruction['points'] and track not in sub_model['points']:
                sub_model['points'][track] = reconstruction['points'][track].copy()
    
    return sub_model

def UpdateModel(reconstruction, sub_model):
    for shot in sub_model['shots']:
        reconstruction['shots'][shot] = sub_model['shots'][shot]
    for track in sub_model['points']:
        reconstruction['points'][track] = sub_model['points'][track]
    return
