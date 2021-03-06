# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

sysUpTime = {
#    UP            .1.3.6.1.2.1.1.3.0					sysUpTimeInstance
    'UP.'       : '.1.3.6.1.2.1.1.3.0'
}

FWVer = {
#    FW            .1.3.6.1.4.1.171.12.1.2.7.1.2			swMultiImageVersion
    'FW.'       : '.1.3.6.1.4.1.171.12.1.2.7.1.2.1'
}

Errors = {
#    RX_crc        .1.3.6.1.2.1.16.1.1.1.8				etherStatsCRCAlignErrors
    'RX_crc.1'  : '.1.3.6.1.2.1.16.1.1.1.8.1',
    'RX_crc.2'  : '.1.3.6.1.2.1.16.1.1.1.8.2',
    'RX_crc.3'  : '.1.3.6.1.2.1.16.1.1.1.8.3',
    'RX_crc.4'  : '.1.3.6.1.2.1.16.1.1.1.8.4',
    'RX_crc.5'  : '.1.3.6.1.2.1.16.1.1.1.8.5',
    'RX_crc.6'  : '.1.3.6.1.2.1.16.1.1.1.8.6',
    'RX_crc.7'  : '.1.3.6.1.2.1.16.1.1.1.8.7',
    'RX_crc.8'  : '.1.3.6.1.2.1.16.1.1.1.8.8',
    'RX_crc.9'  : '.1.3.6.1.2.1.16.1.1.1.8.9',
    'RX_crc.10' : '.1.3.6.1.2.1.16.1.1.1.8.10',
}

RxTx = {
#     RX           .1.3.6.1.2.1.31.1.1.1.6				ifHCInOctets
    '~RX.1'     : '.1.3.6.1.2.1.31.1.1.1.6.1',
    '~RX.2'     : '.1.3.6.1.2.1.31.1.1.1.6.2',
    '~RX.3'     : '.1.3.6.1.2.1.31.1.1.1.6.3',
    '~RX.4'     : '.1.3.6.1.2.1.31.1.1.1.6.4',
    '~RX.5'     : '.1.3.6.1.2.1.31.1.1.1.6.5',
    '~RX.6'     : '.1.3.6.1.2.1.31.1.1.1.6.6',
    '~RX.7'     : '.1.3.6.1.2.1.31.1.1.1.6.7',
    '~RX.8'     : '.1.3.6.1.2.1.31.1.1.1.6.8',
    '~RX.9'     : '.1.3.6.1.2.1.31.1.1.1.6.9',
    '~RX.10'    : '.1.3.6.1.2.1.31.1.1.1.6.10',
#     TX           .1.3.6.1.2.1.31.1.1.1.10				ifHCOutOctets
    '~TX.1'     : '.1.3.6.1.2.1.31.1.1.1.10.1',
    '~TX.2'     : '.1.3.6.1.2.1.31.1.1.1.10.2',
    '~TX.3'     : '.1.3.6.1.2.1.31.1.1.1.10.3',
    '~TX.4'     : '.1.3.6.1.2.1.31.1.1.1.10.4',
    '~TX.5'     : '.1.3.6.1.2.1.31.1.1.1.10.5',
    '~TX.6'     : '.1.3.6.1.2.1.31.1.1.1.10.6',
    '~TX.7'     : '.1.3.6.1.2.1.31.1.1.1.10.7',
    '~TX.8'     : '.1.3.6.1.2.1.31.1.1.1.10.8',
    '~TX.9'     : '.1.3.6.1.2.1.31.1.1.1.10.9',
    '~TX.10'    : '.1.3.6.1.2.1.31.1.1.1.10.10',
}

DuplexStatus = {
#    DS            .1.3.6.1.2.1.10.7.2.1.19				dot3StatsDuplexStatus
    'DS.1'      : '.1.3.6.1.2.1.10.7.2.1.19.1',
    'DS.2'      : '.1.3.6.1.2.1.10.7.2.1.19.2',
    'DS.3'      : '.1.3.6.1.2.1.10.7.2.1.19.3',
    'DS.4'      : '.1.3.6.1.2.1.10.7.2.1.19.4',
    'DS.5'      : '.1.3.6.1.2.1.10.7.2.1.19.5',
    'DS.6'      : '.1.3.6.1.2.1.10.7.2.1.19.6',
    'DS.7'      : '.1.3.6.1.2.1.10.7.2.1.19.7',
    'DS.8'      : '.1.3.6.1.2.1.10.7.2.1.19.8',
    'DS.9'      : '.1.3.6.1.2.1.10.7.2.1.19.9',
    'DS.10'     : '.1.3.6.1.2.1.10.7.2.1.19.10',
}

CPUutil = {
#    CPU           .1.3.6.1.4.1.171.12.1.1.6.3				agentCPUutilizationIn5min
    'CPU.'      : '.1.3.6.1.4.1.171.12.1.1.6.3.0'
}

CNS = {
#    CNS           .1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4		swL2PortCtrlNwayState
    'CNS..1'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.1.100',
    'CNS..2'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.2.100',
    'CNS..3'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.3.100',
    'CNS..4'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.4.100',
    'CNS..5'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.5.100',
    'CNS..6'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.6.100',
    'CNS..7'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.7.100',
    'CNS..8'    : '.1.3.6.1.4.1.171.11.113.1.1.2.2.2.1.4.8.100',
}

CfgUpload = [
#     .1.3.6.1.4.1.171.12.1.2.1.1.3					agentBscSwFileAddr
    ['.1.3.6.1.4.1.171.12.1.2.1.1.3','3','10.200.201.180','IPADDR'],
#     .1.3.6.1.4.1.171.12.1.2.1.1.5					agentBscSwFile
    ['.1.3.6.1.4.1.171.12.1.2.1.1.5','3','backup','OCTETSTR'],
#     .1.3.6.1.4.1.171.12.1.2.1.1.7					agentBscSwFileLoadType
    ['.1.3.6.1.4.1.171.12.1.2.1.1.7','3','2','INTEGER'],
#     .1.3.6.1.4.1.171.12.1.2.1.1.8					agentBscSwFileCtrl
    ['.1.3.6.1.4.1.171.12.1.2.1.1.8','3','3','INTEGER'],
]

CfgSave = [
#     .1.3.6.1.4.1.171.12.1.2.6						agentSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.6', '0', '2', 'INTEGER'],
    ]
