from pyscript import display, document

def sample_function(e): 
    name = document.getElementById('text1').value 
    age = document.getElementById('text2').value 
    school = document.getElementById('text3').value 
    
    display(f' Student Profile:', target='output') 

    display("----------------------", target='output')

    display(f' Name: {name}', target='output') 
    display(f' Age: {age}', target='output') 
    display(f' School: {school}', target='output') 

    display("----------------------", target='output')

    display(f' Note:', target='output') 
    display(f' {name} is currently {age} and studies at {school}. This information was gathered through input fields and displayed using multiline string in Python via PyScript.', target='output')

