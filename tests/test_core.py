import numpy as np
from zambia_prospectivity.prospectivity import prospectivity_class, target_membership

def test_prospectivity_classes():
    score = np.array([0.2, 0.5, 0.79, 0.8, 1.0])
    assert prospectivity_class(score).tolist() == ["Low","Medium","Medium","High","High"]
    u = np.array([[0.2,0.8],[0.7,0.3]])
    assert np.allclose(target_membership(u, 1), [0.8,0.3])
