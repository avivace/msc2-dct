<template>
	<div class="hello">
		<h1>MCS2 - JPEG UI </h1>
		<h2> Antonio Vivace - February 2019 </h2>
		
		<form enctype="multipart/form-data">
		<input type="file" name="sourceImage" @change="filesChange($event.target.files);"
						accept="image/*" class="input-file">
				</form>
		{{ height }} x {{width }}
		<img :src=startingImage width=500 height=500 v-if="startingImage">
		<img :src=outputImage width=500 height=500 v-if="startingImage">

	</div>
</template>

<script>
export default {
	data: function(){ return {
		startingImage: null,
		height: null,
		width: null,
		outputImage:null,
	}},
	methods:{
		filesChange: function(file){
			var reader = new FileReader();

			// Render the selected image
			reader.onload = function(e){
				console.log(e.target.result)
				this.startingImage = e.target.result;
				let image = new Image();
				image.src = e.target.result;
				this.height = image.height;
				this.width = image.width;
			}.bind(this)

			reader.readAsDataURL(file[0]);

			// Upload it to the backend
			var formData = new FormData();
			formData.append("sourceImage", file[0]);
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
		}
	}
}
</script>

<style scoped>

</style>
