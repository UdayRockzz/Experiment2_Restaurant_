#!/usr/bin/env python
# Georgia

import sys
import qi
import os
import time


class PythonAppMain(object):
    subscriber_list = []
    loaded_topic = ""

    def __init__(self, application):
        # Getting a session that will be reused everywhere
        self.application = application
        self.session = application.session
        self.service_name = self.__class__.__name__

        # Getting a logger. Logs will be in /var/log/naoqi/servicemanager/{application id}.{service name}
        self.logger = qi.Logger(self.service_name)


    @qi.nobind
    def start_app(self):
        print "Starting app..."
        self.disable_tracking()
        self.sound_localisation()
        # self.enable_autonomous()
        self.open_screen()
        self.start_dialog()
        self.logger.info("Started!")

    @qi.nobind
    def stop_app(self):

        self.logger.info("Stopping service...")
        self.application.stop()
        self.logger.info("Stopped!")

    @qi.nobind
    def cleanup(self):
        self.logger.info("Cleaning...")
        # @TODO: insert cleaning functions here
        self.disconnect_signals()
        self.stop_dialog()
        self.stop_screen()
        self.logger.info("Cleaned!")

    @qi.nobind
    def create_signals(self):
        self.logger.info("Creating MenuChosen event...")
        memory = self.session.service("ALMemory")
        
        event_name = "TabChosen/Name"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_tab_chosen)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("Tab Event created!")
        
        event_name = "TabChosen/Exit"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_exit)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("Event Exit!")

        event_name = "UserChosen/Name"
        memory.declareEvent(event_name)
        event_subscriber = memory.subscriber(event_name)
        event_connection = event_subscriber.signal.connect(self.on_event_user_touch)
        self.subscriber_list.append([event_subscriber, event_connection])
        self.logger.info("Event Exit!")
        
        
    @qi.nobind
    def disconnect_signals(self):
        self.logger.info("Unsubscribing to all events...")
        for sub, i in self.subscriber_list :
            try:
                sub.signal.disconnect(i)
            except Exception as e:
                self.logger.info("Error unsubscribing: {}".format(e))
        self.logger.info("Unsubscribe done!")

    @qi.nobind
    def start_dialog(self):
        self.logger.info("Loading dialog")
        dialog = self.session.service("ALDialog")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        topic_path = os.path.realpath(os.path.join(dir_path, "Experiment2", "Experiment2_enu.top"))
        #topic_path = "/home/nao/georgia-pepper/dialog_files/Experiment1_enu.top"
        self.logger.info("File is: {}".format(topic_path))
        try:
            self.loaded_topic = dialog.loadTopic(topic_path)
            dialog.activateTopic(self.loaded_topic)
            dialog.subscribe(self.service_name)
            self.logger.info("Dialog loaded!")
        except Exception as e:
            self.logger.info("Error while loading dialog: {}".format(e))

    @qi.nobind
    def stop_dialog(self):
        self.logger.info("Unloading dialog")
        try:
            dialog = self.session.service("ALDialog")
            dialog.unsubscribe(self.service_name)
            dialog.deactivateTopic(self.loaded_topic)
            dialog.unloadTopic(self.loaded_topic)
            self.logger.info("Dialog unloaded!")
        except Exception as e:
            self.logger.info("Error while unloading dialog: {}".format(e))

    @qi.nobind
    def open_screen(self):
        folder = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.logger.info("Loading tablet page for app: {}".format(folder))
        try:
            ts = self.session.service("ALTabletService")
            ts.loadApplication(folder)
            ts.showWebview()
            self.logger.info("Tablet loaded!")
        except Exception as e:
            self.logger.info("Error while loading tablet: {}".format(e))

    @qi.nobind
    def stop_screen(self):
        self.logger.info("Unloading tablet...")
        try:
            tablet = self.session.service("ALTabletService")
            tablet.hideWebview()
            self.logger.info("Tablet unloaded!")
        except Exception as e:
            self.logger.info("Error while unloading tablet: {}".format(e))
    
    @qi.nobind
    def disable_tracking(self):
        self.logger.info("Disable Face tracking...")
        try:
            tracking = self.session.service("ALBasicAwareness")
            tracking.stopAwareness()
            self.logger.info("Tracking Disabled")
        except Exception as e:
            self.logger.info("Error while disabling tracking: {}".format(e))
    
    @qi.nobind
    def enable_autonomous(self):
        self.logger.info("Enable Autonomous...")
        try:
            life_service = self.session.service("ALAutonomousLife")
            life_service.setAutonomousAbilityEnabled("BasicAwareness", True)
            self.logger.info("Autonomous Enabled")
        except Exception as e:
            self.logger.info("Error while enabling autonomous: {}".format(e))

    @qi.nobind
    def sound_localisation(self):
        self.logger.info("Localising Sound...")
        try:
            sound_detect_service = self.session.service("ALSoundDetection")
            sound_detect_service.setParamter("Sensitivity", 0.3)
            self.logger.info("Autonomous Enabled")
        except Exception as e:
            self.logger.info("Error while enabling autonomous: {}".format(e))

    @qi.bind(methodName="onEventTabChosen", paramsType=(qi.String,), returnType=qi.Void)
    def on_event_tab_chosen(self, tab):
        if tab:
            self.logger.info("Tab Chosen by event: {}".format(tab))
            self.stop_dialog()
            #What to do here
            time.sleep(2)
            self.start_dialog()

            
    @qi.bind(methodName="onExit", returnType=qi.Void)
    def on_exit(self, value):
        self.stop_app()

if __name__ == "__main__":
    # with this you can run the script for tests on remote robots
    # run : python main.py --qi-url 123.123.123.123
    app = qi.Application(sys.argv)
    app.start()
    service_instance = PythonAppMain(app)
    service_id = app.session.registerService(service_instance.service_name, service_instance)
    service_instance.start_app()
    app.run()
    service_instance.cleanup()
    app.session.unregisterService(service_id)
