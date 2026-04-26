document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("formulario");

    form.addEventListener("submit", async function(e){
        e.preventDefault();
        
        let edad = parseInt(document.getElementById("edad").value);
        let genero = document.getElementById("genero").value;
        let departamento = document.getElementById("departamento").value;
        let cgpa = parseFloat(document.getElementById("cgpa").value);
        let sueno = parseFloat(document.getElementById("sueno").value);
        let estudio = parseFloat(document.getElementById("estudio").value);
        let redes = parseFloat(document.getElementById("redes").value);
        let actividad = parseFloat(document.getElementById("actividad").value);
        let estres = parseFloat(document.getElementById("estres").value);

        try {
            let response = await fetch("http://127.0.0.1:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    edad,
                    genero,
                    departamento,
                    cgpa,
                    sueno,
                    estudio,
                    redes,
                    actividad,
                    estres
                })
            });

            if (!response.ok) {
                throw new Error("Error en el servidor");
            }

            let data = await response.json();

            console.log("Predicción:", data.prediccion);

            // Guardar resultado
            localStorage.setItem("prediccion", data.prediccion);

            // Redirigir
            window.location.href = "resultado.html";

        } catch (error) {
            console.error("Error:", error);
            alert("No se pudo conectar con el servidor");
        }

    });

});