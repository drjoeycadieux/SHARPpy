import os
import pytest
import sys
import numpy as np

has_display = os.environ.get('DISPLAY_AVAIL', None) not in ('NO', '0', 'False') and os.environ.get('DISPLAY', None) is not None

if has_display:
    from qtpy import QtGui, QtCore, QtWidgets
    import sharppy.viz as viz
    import sharppy.viz.preferences as preferences
    from sharppy.io.spc_decoder import SPCDecoder

    dec = SPCDecoder('examples/data/14061619.OAX')
    prof_coll = dec.getProfiles()
    prof = prof_coll.getCurrentProfs()['']

    if QtWidgets.QApplication.instance() is None:
        app = QtWidgets.QApplication([])
    else:
        app = QtWidgets.QApplication.instance()
else:
    viz = None
    prof = None
    app = None

@pytest.mark.skipif(not has_display, reason="DISPLAY not set")
def test_insets():
    insets = [viz.fire.plotFire,
              viz.winter.plotWinter,
              viz.kinematics.plotKinematics,
              viz.stp.plotSTP,
              viz.ship.plotSHIP,
              viz.vrot.plotVROT,
              viz.analogues.plotAnalogues,
              viz.stpef.plotSTPEF]
    names = ['fire', 'winter', 'kinematics', 'stp', 'ship', 'vrot', 'sars', 'stpef']
    for inset, name in zip(insets, names):
        print("Testing:", str(inset))
        if inset is viz.thermo.plotText:
            test = inset(['SFC', 'ML', 'MU', 'FCST'])
        else:
            test = inset()
        test.setProf(prof)
        test.setGeometry(50,50,293,195)
        test.plotBitMap.save(name + '_test.png', format='png')
        del test

    ens = viz.ensemble.plotENS()
    ens.addProfileCollection(prof_coll)
    ens.setActiveCollection(0)

@pytest.mark.skipif(not has_display, reason="DISPLAY not set")
def test_hodo():
    hodo = viz.hodo.plotHodo

    s = hodo()
    s.addProfileCollection(prof_coll)
    s.setActiveCollection(0)
    #s.setMWCenter()
    #s.setSRCenter()
    #s.setDeviant('left')
    s.plotBitMap.save('hodo.png', format='png')

@pytest.mark.skipif(not has_display, reason="DISPLAY not set")
def test_skew():
    skew = viz.skew.plotSkewT
    #s = skew()
    #s.addProfileCollection(prof_coll)
    #s.setActiveCollection(0)
    #s.plotBitMap.save('skew.png', format='png')

@pytest.mark.skipif(not has_display, reason="DISPLAY not set")
def test_smaller_insets():
    insets = [viz.speed.plotSpeed,
              viz.advection.plotAdvection,
              viz.watch.plotWatch,
              viz.srwinds.plotWinds,
              viz.slinky.plotSlinky,
              viz.thetae.plotThetae]
    names = ['speed', 'advection', 'watch', 'srwinds', 'slinky', 'thetae']
    for inset, name in zip(insets, names):
        print("Testing:", str(inset))
        test = inset()
        test.setProf(prof)
        if name == 'slinky':
            test.setParcel(prof.mupcl)
            test.setDeviant('left')
        test.setGeometry(50,50,293,195)
        test.plotBitMap.save(name + '_test.png', format='png')
        del test

    test = viz.generic.plotGeneric(np.asarray([1,2]),np.asarray([1,2]))
    del test

@pytest.mark.skipif(not has_display, reason="DISPLAY not set")
def test_mapper():
    mapper = viz.map.Mapper(-97,35)
    assert mapper.getLambda0() == -97
    assert mapper.getPhi0() == 35
    mapper.setLambda0(-97)
    for proj in ['npstere', 'spstere', 'merc']:
        mapper.setProjection(proj)
        assert mapper.getProjection() == proj
        mapper.getCoordPaths()

if app is not None:
    app.quit()
    del app
