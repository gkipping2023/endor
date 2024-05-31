function myFunction() {
    let text = document.getElementById("block1").value;
    const myArray = text.split(":");
    let decimal = myArray[1] / 60;
    let result = Number(decimal) + Number(myArray[0])
    let finalDecimal = result.toFixed(2)
    document.getElementById("demo").innerHTML = finalDecimal;
}
//Unused
// function myFunction2() {
//     const ctx = document.getElementById('myChart');
      
//         new Chart(ctx, {
//           type: 'bar',
//           data: {
//             datasets: [{
//               data: {{months_data|safe}},
//               label: 'Hours by Month',
//               borderWidth: 1
//             },{
//               type: 'line',
//               label: '80h Goal',
//               data: [80,80,80,80,80,80,80,80,80,80,80,80,]
//             }
//           ],
//             labels : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Nov','Dec'],
//           },
//           options: {
//             scales: {
//               y: {
//                 beginAtZero: true,
//                 max: 100
//               }
//             }
//           }
//         });
// }