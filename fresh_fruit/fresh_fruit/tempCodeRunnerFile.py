on():
    vid = cv2.VideoCapture(0)
    
    while(vid.isOpened()):

        start = time.time()

        ret, frame = vid.read()
        prediction = cv2.resize(frame,(200,200))
        new_pred = np.expand_dims(prediction,axis = 0)

        # Font type of the displayed text
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        val = new_model.predict(new_pred)

        end = time.time()

        total_time = end-start
        fps = 1/total_time
        if(val==0):
            cv2.putText(frame, 
                    'Fresh Fruit', 
                    (50, 50), 
                    font, 1, 
                    (0, 255, 0), 
                    2, 
                    cv2.LINE_4)
        else:
            cv2.putText(frame, 
                'Rotten Fruit', 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
        print(val)

        cv2.putText(frame, 
            f'FPS: {int(fps)}', 
            (100, 100), 
            font, 1, 
            (0, 100, 255), 
            2, 
            cv2.LINE_4)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()