1. ref: https://github.com/macTracyHuang/NTU-ML2022-Spring/blob/main/Hw6/ML_HW6%20try%20style.ipynb
        https://github.com/lucidrains/stylegan2-pytorch
	直接用stylegan2

2. 原本助教給的資料集(70000多張圖)有點髒，在同樣的網站上找到另外一份動漫頭像(20000多張)但乾淨很多
   https://huggingface.co/datasets/huggan/anime-faces

3. 用server跑stylegan, 沒有改參數，預設15萬步。使用顯卡NVIDIA GeForce RTX 2080 SUPER, 共耗時約43hr1

4. 跑完之後generate出了3000張圖(1000*3), 從server上抓下來之後用rng.py挑選其中的1000張，用move把這1000張改成上傳形式(1.jpg, 2.jpg....)

5. 因為是拉到windows上面處理步驟4，所以生成出1000張之後不用程式，直接ctrl+a右鍵壓縮

6. 壓縮檔有附上使用的資料集(data), 20000多張圖片

7. 如果想在排行榜上得名的話，請把這些圖片(1000張頭像) 壓成一張圖(一張圖有1000顆頭), 然後剩下的99張圖都放一顆頭，這樣你的成績會超過100