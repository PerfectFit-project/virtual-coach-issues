Feature: Rasa Chat recommendations

  Scenario: Get user km run target
     Given rasa bot is up and running
      When we ask for the agenda
      Then all messages are found to be addressed to the user
       And advice on running distance is given
