import login_main
import pytest

#testing for language choice and creating a job for an existing user

    #create job -- choice 8
def test_for_job_choices(capsys):
    input_values = [2 , "Kevin", "Keval@1997", "Kevin", "Zhang", 1, "Kevin","Keval@1997" , 8, "Student", "Tesla", "10/05/2021", "10/09/2021", "Texas", "I worked in the IT department", "", ]

    def mock_input(s):
        return input_values.pop(0)

    login_main.input = mock_input

    with pytest.raises(OSError):
        login_main.main()


    out, err = capsys.readouterr()

    assert out ==  """--------------- Login Page ---------------
        Please Select One of the Following Options

        1. Login Using Existing InCollege Account
        2. Create a New InCollege Account
        3. InCollege Important Links
        4. Useful Links
        
        lease choose one to learn more about
1. General
2. Browse InCollege
3. Business Solutions
4. Directories
5. Return
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

We're here to help
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

In College Pressroom: Stay on top of the latest news, updates, and reports
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

Under construction
1. Sign Up
2. Help Center
3. About
4. Press
5. Blog
6. Careers
7. Developers
8. Return

    
    
        """
    assert err == ' '




