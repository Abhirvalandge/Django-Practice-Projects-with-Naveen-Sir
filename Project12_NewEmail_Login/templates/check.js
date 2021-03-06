
function validate()
{
    // Reading Value From Password Input Field
    var password = document.getElementById("p1").value

    // Finding the length of password
    var p_len = password.length

    if (p_len < 8)
    {
        document.getElementById("s1").innerText="Poor"
        document.getElementById("s2").innerText=""
        document.getElementById("s3").innerText=""
    }
    else
        {
        if (p_len == 8)
        {
            document.getElementById("s1").innerText=""
        document.getElementById("s2").innerText="Good"
        document.getElementById("s3").innerText=""
        }
        else {
            document.getElementById("s1").innerText=""
        document.getElementById("s2").innerText=""
        document.getElementById("s3").innerText="Strong"
        }
    }

}