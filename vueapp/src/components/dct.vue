<template>
	<div class="hello">
		  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
    	<v-flex xs12>
		<center><h1 style="font-size:64px; font-weight: 300">MCS2 - DCT2 UI </h1></center>
		<span style="font-size:18px;font-weight: 400"> Antonio Vivace,  February 2019</span>
		
		<form enctype="multipart/form-data">
		<input type="file" name="sourceImage" @change="filesChange($event.target.files);"
						accept="image/*" class="input-file">
				</form>
    	</v-flex>
      <v-flex xs6 v-if="startingImage">
      	<span style="font-size:24px">Source</span>
        		<img width="100%" :src=startingImage >
      </v-flex>
      	
            <v-flex xs6 v-if="startingImage">
            	      	<span style="font-size:24px">Processed</span>

        		<img width="100%" :src=outputImage >

      </v-flex>
      <v-flex xs12 v-if="startingImage">
      	    <v-btn
      :loading="loading"
      :disabled="loading"
      
      @click="update"
    >
      Applica
    </v-btn>

      </v-flex>
    </v-layout>
  </v-container>
		<div class="slidecontainer">
			<template v-if="imageReady">
			{{ height }} x {{width }}
  d <input type="range" min="0" :max="height+width-2" v-model="d" class="slider" id="dSlider"> {{ d}} <br>
  b <input type="number" step="1" v-model="beta">
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
		beta:1,
		loading: false,
		loader: null,
	}},
	methods:{
		update: function(){
			// Upload it to the backend
			this.loading = true;
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
				self.outputImage = response.data.image
				self.loading = false;
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
				//console.log(e.target.result)
				this.startingImage = e.target.result;
				let image = new Image();
				image.src = e.target.result;
				//console.log(image)

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

<style>
@import url('https://rsms.me/inter/inter.css');
html { font-family: 'Inter', sans-serif; }
@supports (font-variation-settings: normal) {
  html { font-family: 'Inter var', sans-serif; }
}
html{
	font-family: 'Inter';
}
img{
  
  -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 2px 5px;
  -moz-box-shadow: rgba(0,0,0,0.5) 0 2px 5px;
  box-shadow: rgba(0, 0, 0, 0.5) 0 2px 5px;
}
</style>
