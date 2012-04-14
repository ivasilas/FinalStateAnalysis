import FWCore.ParameterSet.Config as cms
import FinalStateAnalysis.Selectors.selectors.selectors as selectors

_binary_bins = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(1.5),
    nbins = cms.untracked.int32(2),
)

def get_trigger_matching(trg_name):
    output = cms.PSet(
        _binary_bins,
        name = cms.untracked.string(
            getattr(selectors.electrons, trg_name).name.value()),
        description = cms.untracked.string(
            getattr(selectors.electrons, trg_name).description.value()),
        plotquantity = cms.untracked.string(
            getattr(selectors.electrons, trg_name).plottable.value()),
        lazyParsing = cms.untracked.bool(False),
    )
    return output

id = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_${eID}"),
    description = cms.untracked.string("${nicename} Electron ID"),
    plotquantity = cms.untracked.string(selectors.electrons.id.plottable.value()),
    lazyParsing = cms.untracked.bool(True),
)

wwid = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_WWID"),
    description = cms.untracked.string("${nicename} Electron WWID"),
    plotquantity = cms.untracked.string(
        selectors.electrons.id.plottable.value().replace('${eID}', 'WWID')),
    lazyParsing = cms.untracked.bool(True),
)

mitid = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_MITID"),
    description = cms.untracked.string("${nicename} Electron MITID"),
    plotquantity = cms.untracked.string(
        selectors.electrons.id.plottable.value().replace('${eID}', 'MITID')),
    lazyParsing = cms.untracked.bool(True),
)

deltaEtaSuperClusterTrack = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_DeltaEta"),
    description = cms.untracked.string("${nicename} Electron DeltaEta"),
    plotquantity = cms.untracked.string(
        '(${getter}deltaEtaSuperClusterTrackAtVtx)'
    ),
    lazyParsing = cms.untracked.bool(True),
)

chargeIdTight = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_Charge_Tight"),
    description = cms.untracked.string("${nicename} Electron Charge tight"),
    plotquantity = cms.untracked.string(
        '(${getter}isGsfCtfScPixChargeConsistent)'
    ),
    lazyParsing = cms.untracked.bool(True),
)

chargeIdMedium = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_Charge_Medium"),
    description = cms.untracked.string("${nicename} Electron Charge tight"),
    plotquantity = cms.untracked.string(
        '(${getter}isGsfScPixChargeConsistent())'
    ),
    lazyParsing = cms.untracked.bool(True),
)

chargeIdLoose = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_Charge_Loose"),
    description = cms.untracked.string("${nicename} Electron Charge loose"),
    plotquantity = cms.untracked.string(
        '(${getter}isGsfCtfChargeConsistent())'
    ),
    lazyParsing = cms.untracked.bool(True),
)

deltaPhiSuperClusterTrack = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_DeltaPhi"),
    description = cms.untracked.string("${nicename} Electron DeltaPhi"),
    plotquantity = cms.untracked.string(
        '(${getter}deltaPhiSuperClusterTrackAtVtx)'
    ),
    lazyParsing = cms.untracked.bool(True),
)

sigmaIEta = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_SigmaIEta"),
    description = cms.untracked.string("${nicename} Electron SigmaIEta"),
    plotquantity = cms.untracked.string(
        '${getter}sigmaIetaIeta'
    ),
    lazyParsing = cms.untracked.bool(True),
)

hOverE = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_EID_HOverE"),
    description = cms.untracked.string("${nicename} Electron HOverE"),
    plotquantity = cms.untracked.string(
        '${getter}hadronicOverEm'
    ),
    lazyParsing = cms.untracked.bool(True),
)

hasConversion = cms.PSet(
    _binary_bins,
    name = cms.untracked.string("${name}_hasConversion"),
    description = cms.untracked.string("${nicename} Electron has conversion"),
    plotquantity = cms.untracked.string('${getter}userFloat("hasConversion")'),
    lazyParsing = cms.untracked.bool(True),
)

# This is not DB corrected, or PF!
reliso = cms.PSet(
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(2),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_ERelIsoBad"),
    description = cms.untracked.string("${nicename} Electron Rel. Iso"),
    plotquantity = cms.untracked.string(
        selectors.electrons.reliso.plottable.value()),
    lazyParsing = cms.untracked.bool(True),
)

relpfiso = cms.PSet(
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(2),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_ERelIso"),
    description = cms.untracked.string("${nicename} Electron Rel. Iso"),
    plotquantity = cms.untracked.string(
        "({getter}chargedHadronIso"
        "+max({getter}photonIso()"
        "+{getter}neutralHadronIso()"
        "-0.5*{getter}particleIso(),0.0))"
        "/{getter}pt()"
    ),
    lazyParsing = cms.untracked.bool(True),
)

jetPt = cms.PSet(
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(200),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_JetPt"),
    description = cms.untracked.string("${nicename} JetPt"),
    plotquantity = cms.untracked.string("${getter}userFloat('jetPt')"),
    lazyParsing = cms.untracked.bool(True),
)
rawJetPt = cms.PSet(
    min = cms.untracked.double(0.0),
    max = cms.untracked.double(200),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_RawJetPt"),
    description = cms.untracked.string("${nicename} JetPt"),
    plotquantity = cms.untracked.string(
        '? ${getter}userCand("patJet").isNonnull ? '
        '${getter}userCand("patJet").userCand("uncorr").pt : userFloat("jetPt")'),
    lazyParsing = cms.untracked.bool(True),
)

btag = cms.PSet(
    min = cms.untracked.double(-10),
    max = cms.untracked.double(10),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_EBtag"),
    description = cms.untracked.string("${nicename} electron seed jet b-tag"),
    plotquantity = cms.untracked.string(
        '? ${getter}userCand("patJet").isNonnull ? '
        '${getter}userCand("patJet").bDiscriminator("") : -5'),
    lazyParsing = cms.untracked.bool(True),
)

btagmuon = cms.PSet(
    min = cms.untracked.double(-10),
    max = cms.untracked.double(10),
    nbins = cms.untracked.int32(200),
    name = cms.untracked.string("${name}_EBtagSoftMuon"),
    description = cms.untracked.string("${nicename} electron seed jet b-tag"),
    plotquantity = cms.untracked.string(
        '? ${getter}userCand("patJet").isNonnull ? '
        '${getter}userCand("patJet").bDiscriminator("softMuonByIP3dBJetTagsAOD") : -5'),
    lazyParsing = cms.untracked.bool(True),
)

missingHits = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(10.5),
    nbins = cms.untracked.int32(11),
    name = cms.untracked.string("${name}_MissingHits"),
    description = cms.untracked.string("${nicename} electron missing hits"),
    plotquantity = cms.untracked.string(
        '? ${getter}gsfTrack.isNonnull? '
        '${getter}gsfTrack.trackerExpectedHitsInner.numberOfHits() : 10'),
    lazyParsing = cms.untracked.bool(True),
)

cicLoose = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(10.5),
    nbins = cms.untracked.int32(11),
    name = cms.untracked.string("${name}_cicLoose"),
    description = cms.untracked.string("${nicename} cicLoose"),
    plotquantity = cms.untracked.string(
        '${getter}electronID("cicLoose")'),
    lazyParsing = cms.untracked.bool(True),
)

cicMedium = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(10.5),
    nbins = cms.untracked.int32(11),
    name = cms.untracked.string("${name}_cicMedium"),
    description = cms.untracked.string("${nicename} cicMedium"),
    plotquantity = cms.untracked.string(
        '${getter}electronID("cicMedium")'),
    lazyParsing = cms.untracked.bool(True),
)

cicTight = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(10.5),
    nbins = cms.untracked.int32(11),
    name = cms.untracked.string("${name}_cicTight"),
    description = cms.untracked.string("${nicename} cicTight"),
    plotquantity = cms.untracked.string(
        '${getter}electronID("cicTight")'),
    lazyParsing = cms.untracked.bool(True),
)

cicHyperTight = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(10.5),
    nbins = cms.untracked.int32(11),
    name = cms.untracked.string("${name}_cicHyperTight1"),
    description = cms.untracked.string("${nicename} cicHyperTight1"),
    plotquantity = cms.untracked.string(
        '${getter}electronID("cicHyperTight1")'),
    lazyParsing = cms.untracked.bool(True),
)

muonoverlap = cms.PSet(
    min = cms.untracked.double(-0.5),
    max = cms.untracked.double(0.5),
    nbins = cms.untracked.int32(2),
    name = cms.untracked.string("${name}_MuonOverlap"),
    description = cms.untracked.string("${nicename} muon overlap"),
    plotquantity = cms.untracked.string(
        'filteredOverlaps(${index}, "muons", "pt > 5 & abs(eta) < 2.1 & userInt(\'WWID\') > 0.5").size()'),
    lazyParsing = cms.untracked.bool(True),
)

# Add all the interesting electron trigger filter matchings
hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter = get_trigger_matching(
    'hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter')

hltMu17Ele8CaloIdTPixelMatchFilter = get_trigger_matching(
    'hltMu17Ele8CaloIdTPixelMatchFilter')

hltL1NonIsoHLTNonIsoMu8Ele17PixelMatchFilter = get_trigger_matching(
    'hltL1NonIsoHLTNonIsoMu8Ele17PixelMatchFilter')

hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter = get_trigger_matching(
    'hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter')

all = [
    reliso, relpfiso, wwid, mitid, jetPt, rawJetPt, btag, btagmuon, missingHits,
    hasConversion, muonoverlap,
    chargeIdTight, chargeIdMedium, chargeIdLoose,
    deltaEtaSuperClusterTrack, deltaPhiSuperClusterTrack, sigmaIEta, hOverE,
    cicLoose, cicMedium, cicTight, cicHyperTight,
    hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter,
    hltMu17Ele8CaloIdTPixelMatchFilter,
    hltL1NonIsoHLTNonIsoMu8Ele17PixelMatchFilter,
    hltMu8Ele17CaloIdTCaloIsoVLPixelMatchFilter,
]
