import json

className= ['Accessories','AdjustmentAngles','AgeGroup','AudioChipset','AudioCodecSupport','AudioFileFormats','AudioFormat','AudioPecularities','Authentication','BacklightColor','Barcodes','BatteryFormFactor','BatterySystem','BatteryType','BluetoothCodec','BluetoothProfile','BluetoothVersion','Brand','CableConnectors','CacheLevel','Cellular','Chuck','CitylinkDictionary','CityMassUpload','Coating','Color','ColorDepth','CommercialType','CompatibleBrands','CompatibleDevices','CompatibleManufacturers','CompatiblePrinters','Connector','ContactlessPay','Contrast','Country','CPU','CPUChipset','CPUCodename','CPUManufacturer','CPUModel','CPUName','CPUSocket','DiscreteGPU','DisplayColorsQty','DisplayFeatures','DisplayTechnology','DisplayType','Distributor','DocFileFormats','EnergyConsumptionClass','EngineDesign','EngineType','ExpansionSlot','FastChargeStandard','FlashMemoryType','Fonts','Frequency','GameConsoles','Gender','GPU','GPUManufacturer','GPUPowerConnectors','HandleType','HDRFormats','HDRStandards','Humidity','ImageFileFormats','InputDevice','IntegratedGPU','Interfaces','KeyboardLanguage','LampLighting','LampSocketType','LEDType','MainsVoltage','Mapping','Material','MaterialForTool','MemoryBusWidth','MemoryCardFormat','MemoryFormFactor','MemoryType','MiningAlgo','MobileCPUManufacturer','MobileGPU','MobileGPUManufacturer','MobileOperatingSystem','MobilePlatform','MoblieCPU','Model','MotherboardFormFactor','MotherboardManufacturer','MVideoDictionary','MVideoMassUpload','Navigation','NetworkAdapter','NoiseVibration','OperatingSystem','OpticalDrive','OriginalPN','OzonDictionary','Package','PaperSize','PCIExpressLinesNumber','PCIExpressSize','PCIExpressVersion','PFC','PowerSource','PrintColor','PrintTechnology','Product','ProductLineDrive','ProductLineMemoryCard','ProductLineMobileDevice','ProductLineTV','ProductOffer','Protection','ProtectionClass','RAIDLevels','RAMStandard','RAMVoltage','RMController','SberMassUpload','ScannerLocation','ScanResolution','ScreenBacklightTechnology','ScreenFormat','ScreenProtection','ScreenResolution','Sensors','Series','ShootingMode','SIMCardType','SlotType','SmartHomeControlMethods','SmartHomeControlType','SmartHomeDeviceConnection','SmartHomeEcosystem','SmartHomeNotifications','SmartHomeProtocol','StorageConnector','StorageController','StorageFormFactor','StorageInterface','StorageType','StreamingService','SupportedAPI','SupportedApplication','ThreeDFileFormats','ThreeDPrintingMaterial','ThreeDPrintTechnology','ToolFeatures','TouchscreenTechnology','VESAMount','VideoBus','VideoFileFormats','VideoInterface','VideoMemoryType','VideoQuality','VoiceAssistant','Warranty','WBDictionary','WiFiFrequency','WiFiVersion','WiredNetworkInterface','WirelessChargeStandards','WirelessInterface','WorkingMode','Year','YMarketMassUpload']
print(len(className))
my_dict = {}
for name in className:
    json_data = {
                "id": name,
                "name": name,
                "columnConfig": {
                    "columns": [
                        {
                            "attributes": {
                                "attribute": "key",
                                "label": "Key",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "id",
                                "label": "id",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "fullpath",
                                "label": "fullpath",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "published",
                                "label": "published",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "creationDate",
                                "label": "creationDate",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "modificationDate",
                                "label": "modificationDate",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "filename",
                                "label": "filename",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "classname",
                                "label": "classname",
                                "dataType": "system"
                            },
                            "isOperator": False
                        },
                        {
                            "attributes": {
                                "attribute": "index",
                                "label": "index",
                                "dataType": "system"
                            },
                            "isOperator": False
                        }
                    ]
                }            
        }
    my_dict[name] = json_data
with open('/home/akozlov/Загрузки/data_file.json', 'w') as file:
    json.dump(my_dict, file, indent=4, ensure_ascii=False)

print("JSON файл успешно создан.")