import FWCore.ParameterSet.Config as cms

metTypeCategorization = cms.PSet(
    tauCut = cms.string(
        'pt > 10 && (tauID("decayModeFinding") && tauID("byLooseIsolation"))'
        # below cuts inspired by JetMETCorrections/METPUSubtraction/python/mvaPFMET_leptons_cfi.py
        #'pt > 19 && abs(eta) < 2.3 && (tauID("decayModeFinding") && tauID("byIsolationMVAraw") && tauID("againstElectronLoose") && tauID("againstMuonLoose2"))'
    ),
    jetCut = cms.string(
        '!(tauID("decayModeFinding") && tauID("byLooseIsolation")) && userCand("patJet").pt > 10'
    ),
    # The part about passing the tauID is to catch the low pt taus
    unclusteredCut = cms.string(
        'userCand("patJet").pt < 10 | (pt < 10 && tauID("decayModeFinding") && tauID("byLooseIsolation"))'
    ),
)

systematicsMET = cms.EDProducer(
    "PATMETSystematicsEmbedder",
    src = cms.InputTag("patMETsPF"),
    mvametSrc = cms.InputTag("patMEtMVA"),
    tauSrc = cms.InputTag("fixme"),
    muonSrc = cms.InputTag("fixme"),
    electronSrc = cms.InputTag("fixme"),
    tauCut = metTypeCategorization.tauCut,
    jetCut = metTypeCategorization.jetCut,
    unclusteredCut = metTypeCategorization.unclusteredCut,
    applyType1ForTaus = cms.bool(False),
    applyType1ForMuons = cms.bool(False),
    applyType1ForElectrons = cms.bool(False),
    applyType1ForJets = cms.bool(True),
    applyType2ForJets = cms.bool(False),
)
