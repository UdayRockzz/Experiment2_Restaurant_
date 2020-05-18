<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Experiment1" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Experiment2" src="Experiment2/Experiment2.dlg" />
    </Dialogs>
    <Resources>
        <File name="index" src="html/index.html" />
        <File name="main" src="html/main.js" />
        <File name="main" src="main.py" />
        <File name="styles" src="html/styles.css" />
        <File name="translation_en_US" src="translations/translation_en_US.qm" />
        <File name="deserts" src="html/imgs/deserts.jpg" />
        <File name="drinks" src="html/imgs/drinks.jpg" />
        <File name="lakeside" src="html/imgs/lakeside.jpg" />
        <File name="starter_main" src="html/imgs/starter_main.jpg" />
        <File name="lakeside_header" src="html/imgs/lakeside_header.jpg" />
        <File name="jquery-3.4.1" src="html/jquery-3.4.1.js" />
    </Resources>
    <Topics>
        <Topic name="pythonapplauncher_enu" src="pythonapplauncher/pythonapplauncher_enu.top" topicName="pythonapplauncher" language="en_US" />
        <Topic name="Experiment2_enu" src="Experiment2/Experiment2_enu.top" topicName="Experiment2" language="en_US" />
    </Topics>
    <IgnoredPaths>
        <Path src=".idea/vcs.xml" />
        <Path src=".idea/modules.xml" />
        <Path src=".idea/codeStyles/Project.xml" />
        <Path src=".idea/inspectionProfiles/profiles_settings.xml" />
        <Path src=".idea/Experiment2.iml" />
        <Path src=".idea/codeStyles" />
        <Path src=".idea/misc.xml" />
        <Path src=".idea/workspace.xml" />
        <Path src=".idea" />
        <Path src=".idea/.gitignore" />
        <Path src=".idea/dbnavigator.xml" />
        <Path src=".idea/inspectionProfiles" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
