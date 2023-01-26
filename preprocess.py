
import dlib
import torchvision.transforms

detector = dlib.get_frontal_face_detector()

def face_detect(img):
    img1 = img
    dets = detector.run(img, 1, -1)
    for k in [1, 2, 3]:
        img_rot = torch.rot90(img, k)
        dets_rot = detector.run(img_rot, 1, -1)
        if dets_rot[1][0] > dets[1][0]:
            img1 = img_rot
            dets = dets_rot

    img2 = img1
    for a in range(-60, 61, 5):
        img_rot = torchvision.transfoms.functional.rotate(img1, a)
        dets_rot = detector.run(img_rot, 1, -1)
        if dets_rot[1][0] > dets[1][0]:
            img2 = img_rot
            dets = dets_rot
    return img2, dets[0][0]

def crop_face(img, det):
    #TODO

