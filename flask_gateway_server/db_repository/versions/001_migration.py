from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user1 = Table('user1', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

controller = Table('controller', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('controllerStrId', String(length=64)),
    Column('address', String(length=64)),
    Column('Latitude', Float),
    Column('Longitude', Float),
    Column('categoryStrId', Integer),
    Column('serverMsgUrl_webapp', String(length=256)),
    Column('reportFrequency', Float),
    Column('comment', String(length=256)),
    Column('install_date', String(length=32)),
    Column('InstallStatus', String(length=32)),
    Column('network_section', String(length=32)),
    Column('network_segmentnumber', Integer),
    Column('network_type', String(length=32)),
    Column('networkOperationalKey', String(length=32)),
    Column('ProductId', String(length=32)),
    Column('providerId', Integer),
    Column('reference', Integer),
    Column('SoftwareVersion', String(length=32)),
    Column('SystemInfo', String(length=128)),
    Column('reportTime', String(length=8)),
    Column('rfChannel', Integer),
    Column('SIMCardNumber', String(length=32)),
    Column('cabinet_numberofsegment', Integer),
    Column('cabinet_type', String(length=32)),
    Column('controller_firmwareVersion', String(length=32)),
    Column('controller_host', String(length=32)),
    Column('controller_model', String(length=32)),
    Column('hardwareRevision', String(length=32)),
    Column('RFStrength', Float),
    Column('timeZonePosix1', String(length=64)),
    Column('ntpHost', String(length=64)),
    Column('sc_DNS', String(length=64)),
    Column('sc_dnsbackup', String(length=64)),
    Column('sc_dhcp', Boolean),
    Column('sc_mask', String(length=256)),
    Column('sc_gateway', String(length=256)),
    Column('DigitalInput1', Boolean),
    Column('DigitalInput2', Boolean),
    Column('DigitalOutput1', Boolean),
    Column('DigitalOutput2', Boolean),
    Column('ManualModeOutput1', Boolean),
    Column('ManualModeOutput2', Boolean),
    Column('AnalogModbus1', Float),
    Column('AnalogModbus2', Float),
    Column('AnalogModbus3', Float),
    Column('AnalogModbus4', Float),
    Column('AnalogModbus5', Float),
    Column('AnalogModbus6', Float),
    Column('AnalogModbus7', Float),
    Column('AnalogModbus8', Float),
    Column('InputModbus1', Boolean),
    Column('InputModbus2', Boolean),
    Column('InputModbus3', Boolean),
    Column('InputModbus4', Boolean),
    Column('InputModbus5', Boolean),
    Column('InputModbus6', Boolean),
    Column('InputModbus7', Boolean),
    Column('InputModbus8', Boolean),
    Column('PulseInput1', Float),
    Column('PulseInput2', Float),
    Column('DoorOpen', Boolean),
    Column('FirmwareUpdateStatus', String(length=64)),
    Column('GatewayFailure', Boolean),
    Column('GatewayFailureMessage', String(length=128)),
    Column('GatewayWarning', Boolean),
    Column('GatewayWarningMessage', String(length=128)),
    Column('CommunicationFailure', Boolean),
    Column('bypassFailure_Alarm', Boolean),
    Column('manualBypass_Alrm', Boolean),
    Column('SegmentFailure1', Boolean),
    Column('SegmentFailure2', Boolean),
    Column('SegmentFailure3', Boolean),
    Column('SegmentFailure4', Boolean),
    Column('SegmentFailure5', Boolean),
    Column('SegmentFailure6', Boolean),
    Column('SegmentFailure7', Boolean),
    Column('SegmentFailure8', Boolean),
)

street_light = Table('street_light', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('idOnController', String(length=64)),
    Column('controllerStrId', String(length=64)),
    Column('MacAddress', String(length=64)),
    Column('address', String(length=64)),
    Column('Latitude', Float),
    Column('Longitude', Float),
    Column('dimmingGroupName', String(length=64)),
    Column('brandId', Integer),
    Column('categoryStrId', Integer),
    Column('modelFunctionId', Integer),
    Column('comment', String(length=256)),
    Column('install_date', String(length=32)),
    Column('InstallStatus', String(length=32)),
    Column('network_section', String(length=32)),
    Column('network_segmentnumber', Integer),
    Column('network_type', String(length=32)),
    Column('power', Integer),
    Column('powerCorrection', Integer),
    Column('ProductId', String(length=32)),
    Column('providerId', Integer),
    Column('reference', Integer),
    Column('SoftwareVersion', String(length=32)),
    Column('SystemInfo', String(length=128)),
    Column('pole_numberoflight', Integer),
    Column('pole_type', String(length=32)),
    Column('ballast_brand', String(length=32)),
    Column('ballast_type', String(length=32)),
    Column('luminaire_brand', String(length=32)),
    Column('luminaire_colorcode', String(length=32)),
    Column('luminaire_function', String(length=32)),
    Column('luminaire_model', String(length=32)),
    Column('luminaire_status', String(length=32)),
    Column('LampLevel', Float),
    Column('LampSwitch', Boolean),
    Column('LampCommandLevel', Float),
    Column('LampCommandMode', Integer),
    Column('LampCommandSwitch', Float),
    Column('RunningHours', Float),
    Column('Current', Float),
    Column('LampCurrent', Float),
    Column('MainVoltage', Float),
    Column('LampVoltage', Float),
    Column('MeteredPower', Float),
    Column('LampPower', Float),
    Column('Energy', Float),
    Column('LampEnergy', Float),
    Column('LampRestartCount', Integer),
    Column('CycleCount', Integer),
    Column('BallastTemp', Float),
    Column('DryContactInput', Boolean),
    Column('PowerFactor', Float),
    Column('Temperature', Float),
    Column('Frequency', Float),
    Column('LampFailure', Boolean),
    Column('BallastCommunicationFailure', Boolean),
    Column('BallastFailure', Boolean),
    Column('CapacitorFailure', Boolean),
    Column('CommissioningFailed', Boolean),
    Column('DaliFailure', Boolean),
    Column('DefaultLostNode', Boolean),
    Column('DeviceFailure', Boolean),
    Column('ExternalComFailure', Boolean),
    Column('FlickeringFailure', Boolean),
    Column('HighCurrent', Boolean),
    Column('LowCurrent', Boolean),
    Column('HighLampCurrent', Boolean),
    Column('LowLampCurrent', Boolean),
    Column('HighVoltage', Boolean),
    Column('LowVoltage', Boolean),
    Column('HighLampVoltage', Boolean),
    Column('LowLampVoltage', Boolean),
    Column('HighPower', Boolean),
    Column('LowPower', Boolean),
    Column('LowPowerFactor', Boolean),
    Column('HighLampRunningHours', Boolean),
    Column('HighBallastTemperature', Boolean),
    Column('HighOLCTemperature', Boolean),
    Column('PhotocellStatus', Boolean),
    Column('PhotocellFailure', Boolean),
    Column('RelayFailure', Boolean),
    Column('BackupScheduler', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    pre_meta.tables['user1'].drop()
    post_meta.tables['controller'].create()
    post_meta.tables['street_light'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    pre_meta.tables['user1'].create()
    post_meta.tables['controller'].drop()
    post_meta.tables['street_light'].drop()
