css = '''
<style>

.chat-message {
    display: flex;
    align-items: center;
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}

.chat-message.user {
    background-color: #2b313e;
    
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.chat-message.bot {
    background-color: #475063
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;

  order: 1;
}

.chat-message.user .avatar {
    order: 2;
    margin-left: 10px;
}

.avatar img {
    max-height: 78px;
    max-width: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.bot .avatar {
    margin-right: 10px;
}

.user .avatar {
    margin-left: 10px;
    order: 2;
}

.user .message {
    order: 1;
}
'''

bot_template = '''
<div class="chat-message bot" style="display: flex; align-items: center;">
    <div class="avatar" style="margin-right: 10px;">
        <img src="https://raw.githubusercontent.com/architkaila/Chat-With-Documents/main/assets/chatbot.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user" style="display: flex; align-items: center; justify-content: flex-end;">
    <div class="message" style="order: 1;">{{MSG}}</div>
    <div class="avatar" style="order: 2; margin-left: 10px;">
        <img src="https://raw.githubusercontent.com/architkaila/Chat-With-Documents/main/assets/user.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
</div>
'''
