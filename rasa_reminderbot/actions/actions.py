# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for an assistant that schedules reminders and
# reacts to external events.

from typing import Any, Text, Dict, List
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ReminderScheduled, ReminderCancelled
from rasa_sdk.executor import CollectingDispatcher


class ActionSetReminder(Action):
    """Schedules a reminder"""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        date0 = datetime.datetime.now()
        # reminder_hour = 9
        # date = datetime.datetime(
        #     date0.year,
        #     date0.month,
        #     date0.day,
        #     reminder_hour,
        #     0,
        #     0,
        #     0)
        # if (date0.hour > reminder_hour):
        #     date = date + datetime.timedelta(days=1)
        date = date0 + datetime.timedelta(seconds=10)

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=date,
            entities="",
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionConfirmReminder(Action):
    """Schedules a reminder"""

    def name(self) -> Text:
        return "action_confirm_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # # dispatcher.utter_message(
        #     "I will remind you the high risk situations for smoking at 9:00 every day")

        dispatcher.utter_message(
            "I will remind you the high risk situations for smoking every seconds")

        return []


class ActionReactToReminder(Action):
    """Reminds the user the high risk situations."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            f"Do you foresee any high risk situations for smoking today?")

        return []


class ForgetReminders(Action):
    """Cancels all reminders."""

    def name(self) -> Text:
        return "action_forget_reminders"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Okay, I'll cancel all your reminders.")

        # Cancel all reminders
        return [ReminderCancelled()]
