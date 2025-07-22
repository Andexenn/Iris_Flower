// const btn = document.querySelector("button");
// const inputs = document.querySelectorAll(".infor");
// const result = document.querySelector(".result");

// async function handle_click(e) {
//   e.preventDefault();
//   const features = [...inputs].map((ele) => parseFloat(ele.value));

//   const response = await fetch("/predict", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/x-www-form-urlencoded", // Đảm bảo là kiểu form data
//     },
//     body: new URLSearchParams({
//       sepal_length: features[0],
//       sepal_width: features[1],
//       petal_length: features[2],
//       petal_width: features[3],
//     }),
//   });

//   const data = await response.json();
//   console.log(data);
//   // * display the result
//   // result.classList.remove('hidden');
// }

// btn.addEventListener("click", handle_click);
