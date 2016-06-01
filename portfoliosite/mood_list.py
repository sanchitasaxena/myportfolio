 



  #quiz q1
    q1_play = db.StringProperty()
    q1_lazy = db.StringProperty()
  #quiz q2 Something
    q2p_happy = db.StringProperty()
    q2p_creative = db.StringProperty()
    q2p_adventure = db.StringProperty()
  #quiz q2 Nothing
    q2l_sad = db.StringProperty()
    q2l_sleepy = db.StringProperty()
    q2l_visual = db.StringProperty()
  #quiz q3 Solving for?
    q3_cough = db.StringProperty()
    q3_nocough = db.StringProperty()


# Mood Types Database
 #
    subspecies = db.StringProperty() # Sativa [ play ] or Indica [ lazy ] or Hybrid [ both ]
    mode_of_intake = db.StringProperty() # Puff or Vape
    sativa_precent = db.StringProperty() # sativa or h_sativa
    indica_precent = db.StringProperty() # 




# Results

# . . . 
    #  - list
    #q1_play and q2p_happy and q3_cough then sativa_vape
    #q1_play and q2p_happy and q3_nocough then sativa_puff

    #q1_play, q2p_creative, q3_cough = sativa_vape, h_sativa_vape
    #q1_play, q2p_creative, q3_nocough = sativa_puff, h_sativa_puff

    #q1_play, q2p_adventure, q3_cough = sativa_vape
    #q1_play, q2p_adventure, q3_nocough = sativa_puff


    #q1_lazy, q2l_sad, q3_cough = h_indica_vape
    #q1_lazy, q2l_sad, q3_nocough = h_indiva_puff

    #q1_lazy, q2l_sleepy, q3_cough = indica_vape
    #q1_lazy, q2l_sleepy, q3_nocough = indiva_puff

    #q1_lazy, q2l_visual, q3_cough = indica_vape, h_indica_vape
    #q1_lazy, q2l_visual, q3_nocough = indica_puff, h_indica_puff
 

    # - sativa_vape , sativa_puff , h_sativa_vape , h_sativa_puff , indica_vape