'''

Ntuple branch template sets for trigger selections

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

IMPORTANT NOTE: If you want the logical OR of several paths, separate them 
by '|' rather than by ','. 
(When the Smart Trigger gets a group of paths separated by commas, it uses 
the one with the lowest prescale (taking the first in case of a tie).

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

_trig_template = PSet(
    namePass = 'evt.hltResult("paths")',
    nameGroup = 'evt.hltGroup("paths")',
    namePrescale = 'evt.hltPrescale("paths")',
)

singleLepton_25ns_MC = PSet(
    _trig_template.replace(
        name='singleMu', 
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu20',
        paths=r'HLT_IsoMu20_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu22',
        paths=r'HLT_IsoMu22_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoTkMu20',
        paths=r'HLT_IsoTkMu20_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoTkMu22',
        paths=r'HLT_IsoTkMu22_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu24',
        paths=r'HLT_IsoMu24_v\\d+'
        ),
    _trig_template.replace(
        name='singleE',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+',
        ),
    _trig_template.replace(
        name='singleEeta2p1Loose',
        paths=r'HLT_Ele27_eta2p1_WPLoose_Gsf_v\\d+',
        ),
    _trig_template.replace(
        name='singleE25eta2p1Tight',
        paths=r'HLT_Ele25_eta2p1_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg1', 
        paths=r'HLT_Mu17_TrkIsoVVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg2', 
        paths=r'HLT_Mu8_TrkIsoVVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg1_noiso', 
        paths=r'HLT_Mu17_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg2_noiso', 
        paths=r'HLT_Mu8_v\\d+'
        ),
    _trig_template.replace(
        name='singleE_leg1', 
        paths=r'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleE_leg2', 
        paths=r'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),

    )

singleLepton_25ns = PSet(
    _trig_template.replace(
        name='singleMu', 
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu18',
        paths=r'HLT_IsoMu18_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoTkMu20',
        paths=r'HLT_IsoTkMu20_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoTkMu22',
        paths=r'HLT_IsoTkMu22_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu20',
        paths=r'HLT_IsoMu20_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu22',
        paths=r'HLT_IsoMu22_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu22eta2p1',
        paths=r'HLT_IsoMu22_eta2p1_v\\d+'
        ),
    _trig_template.replace(
        name='singleIsoMu27',
        paths=r'HLT_IsoMu27_v\\d+'
        ),
    _trig_template.replace(
        name='singleE27LooseEr',
        paths=r'HLT_Ele27_eta2p1_WPLoose_Gsf_v\\d+',
        ),
    _trig_template.replace(
        name='singleE27Tight',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+',
        ),
    _trig_template.replace(
        name='singleE23WPLoose',
        paths=r'HLT_Ele23_WPLoose_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='singleE22eta2p1Loose',
        paths=r'HLT_Ele22_eta2p1_WPLoose_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='singleE25eta2p1Tight',
        paths=r'HLT_Ele25_eta2p1_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='singleE25eta2p1Loose',
        paths=r'HLT_Ele25_eta2p1_WPLoose_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='singleE22eta2p1LooseTau20',
        paths=r'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg1', 
        paths=r'HLT_Mu17_TrkIsoVVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg2', 
        paths=r'HLT_Mu8_TrkIsoVVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg1_noiso', 
        paths=r'HLT_Mu17_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu_leg2_noiso', 
        paths=r'HLT_Mu8_v\\d+'
        ),
    _trig_template.replace(
        name='singleE_leg1', 
        paths=r'HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleE_leg2', 
        paths=r'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    )

doubleLepton_25ns = PSet(
    _trig_template.replace(
        name='doubleMu',
        paths=r'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v\\d+|HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='doubleE',
        paths=r'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='doubleE_23_12',
        paths=r'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='singleE23SingleMu8',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleE17SingleMu8',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleESingleMu',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMuSingleE',
        paths=r'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu17SingleE12',
        paths=r'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='singleMu23SingleE12',
        paths=r'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTau40',
        paths=r'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTau35',
        paths=r'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTau32',
        paths=r'HLT_DoubleMediumIsoPFTau32_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTauCmbIso35Reg',
        paths=r'HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTauCmbIso40Reg',
        paths=r'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='doubleTauCmbIso40',
        paths=r'HLT_DoubleMediumCombinedIsoPFTau40_Trk1_eta2p1_v\\d+'
        ),
    _trig_template.replace(
        name='singleE22SingleTau20SingleL1',
        paths=r'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),
    _trig_template.replace(
        name='singleE24SingleTau20',
        paths=r'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v\\d+'
        ),
    _trig_template.replace(
        name='singleE24SingleTau20SingleL1',
        paths=r'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),
    _trig_template.replace(
        name='singleE27SingleTau20SingleL1',
        paths=r'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),
    _trig_template.replace(
        name='singleE32SingleTau20SingleL1',
        paths=r'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),
    _trig_template.replace(
        name='singleE20SingleTau28',
        paths=r'HLT_Ele20_eta2p1_WPLoose_Gsf_LooseIsoPFTau28_v\\d+'
        ),
    _trig_template.replace(
        name='singleE22SingleTau29',
        paths=r'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau29_v\\d+'
        ),
    _trig_template.replace(
        name='singleE24SingleTau30',
        paths=r'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v\\d+'
        ),
    _trig_template.replace(
        name='singleE36SingleTau30',
        paths=r'HLT_Ele36_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v\\d+'
        ),

    )

tripleLepton = PSet(
    _trig_template.replace(
        name='tripleE',
        paths=r'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v\\d+'
        ),
    _trig_template.replace(
        name='doubleESingleMu',
        paths=r'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v\\d+'
        ),
    _trig_template.replace(
        name='doubleMuSingleE',
        paths=r'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v\\d+'
        ),
    _trig_template.replace(
        name='tripleMu',
        paths=r'HLT_TripleMu_12_10_5_v\\d+'
        ),
    )

