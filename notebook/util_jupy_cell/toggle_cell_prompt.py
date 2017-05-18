'''
Description 
This is a cell-piece to put in the bottom of the ipython 

while EXEC it
- it will hide the Code-Cell and the Promp-region of the Jupyter
'''
from IPython.display import HTML

HTML('''<script>
code_show=true;

function code_toggle() {
  if (code_show){
    $('div.input').hide();
    $('div.prompt').hide();
  }
  else {
    $('div.prompt').show();
    $('div.input').show();
    } code_show = !code_show ;

}

$( document ).ready(code_toggle);
</script>

<style>
input {
    width : 100%;
    background-color: gray;
    border: none;
    color: white;
    padding: 1px 1px;
    text-decoration: none;
    margin: 1px 1px;
    cursor: pointer;
}
</style>

<form action="javascript:code_toggle()">
  <input type="submit" value="toggle on/off">
</form>''')