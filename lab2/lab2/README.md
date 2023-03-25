# Project Structure:

# Apps:
    polls:
      polls/
      polls/<int:id>
      polls/create
      polls/delete/<int:id> 
      polls/update/<int:id>
      polls/up/<int:q_id>/<int:user_id>   // up vote
      polls/down/<int:q_id>/<int:user_id> // down vote
    
    users:
      login_user/
      logout_user/
      register_user/

# Authorization:
  - Questions updated or deleted only by thier owner 
  -  you can up or down vote only if you were registered
