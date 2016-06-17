from utils import gui_ini


cfgGui = gui_ini.GuiIns()
cfgGui.Init()

subCfg = cfgGui.get("9194")

print(len(cfgGui._dictgui))
