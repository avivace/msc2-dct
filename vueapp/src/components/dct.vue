<template>
	<div class="hello">
		<h1>MCS2 - JPEG UI </h1>
		<h2> Antonio Vivace - February 2019 </h2>
		
		<form enctype="multipart/form-data">
		<input type="file" name="sourceImage" @change="filesChange($event.target.files);"
						accept="image/*" class="input-file">
				</form>
		
		<img :src=startingImage width=500 height=500 v-if="startingImage">
		<img :src=outputImage width=500 height=500 v-if="startingImage">
		<div class="slidecontainer">
			<template v-if="imageReady">
			{{ height }} x {{width }}
  d <input @change="update" type="range" min="0" :max="height+width-2" v-model="d" class="slider" id="dSlider"> {{ d}} <br>
  b <input @change="update" type="number" step="1" v-model="beta">
</template>
</div>
	</div>
</template>

<script>
export default {
	data: function(){ return {
		startingImage: null,
		height: null,
		width: null,
		outputImage:null,
		d:0,
		imageReady: false,
		imageData: null,
		beta:1
	}},
	methods:{
		update: function(){
			console.log("value changed")
						// Upload it to the backend
			var formData = new FormData();
			formData.append("sourceImage", this.imageData);
			formData.append("d", this.d)
			formData.append("beta", this.beta)
			var self = this;
			this.$axios.post('http://localhost:5000/image', formData, {
				headers: {
					'Content-Type': 'multipart/form-data'
					}
				})  
			.then(function (response) {
				console.log(response.data)
				self.outputImage = response.data.image
			})
			.catch(function (error) {
				console.log(error);
			});
		},
		filesChange: function(file){
			var reader = new FileReader();

			// Render the selected image
			reader.onload = function(e){
				this.imageReady = true,
				console.log(e.target.result)
				this.startingImage = e.target.result;
				let image = new Image();
				image.src = e.target.result;
				console.log(image)

				// Once it's ready, read height and width
				image.onload = function() {
					this.height = image.height;
					this.width = image.width;
				}.bind(this)

			}.bind(this)

			reader.readAsDataURL(file[0]);

			this.imageData = file[0]
		}
	}
}
</script>

<style scoped>

</style>
