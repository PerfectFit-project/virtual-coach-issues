# Rasa periodic reminder bot

This bot shows how to set periodic reminders within Rasa.

It's adapted from the one-time reminder example [reminderbot](https://github.com/RasaHQ/rasa/tree/main/examples/reminderbot), see [the doc](https://rasa.com/docs/rasa/reaching-out-to-user/#reminders) for the explanation about this example.

## How to use this bot?

To train and chat with this bot, execute the following steps:

1. Train a Rasa Open Source model containing the Rasa NLU and Rasa Core models by running:
    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.

2. Run a Rasa SDK action server with
    ```
    rasa run actions
    ```

3. (Option 1) Run Rasa X to talk to your bot. In a separate console window from where you ran the step 2 command:
    ```
    rasa x
    ```

4. (Option 2) To test this example without Rasa X, run a
   [callback channel](https://rasa.com/docs/rasa/connectors/your-own-website#callbackinput).
   In a separate console window from where you ran the step 2 command:
    ```
    python callback_server.py
    ```
   This will run a server that prints the bot's responses to the console.

5. Start your Rasa server in a third console window:
   ```
   rasa run --enable-api
   ```

6. Try the bot. You can then send messages to the bot via the callback channel endpoint:
   ```
   curl -XPOST http://localhost:5005/webhooks/callback/webhook \
        -d '{"sender": "tester", "message": "hello"}' \
        -H "Content-type: application/json"
   ```