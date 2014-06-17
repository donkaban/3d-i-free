Shader "iFree/simplest" 
{	
	SubShader 
	{
	  Pass 
	  { 
	  	GLSLPROGRAM 
	  	#ifdef VERTEX
        varying vec2 textureCoordinates;
       
	     void main() 
         {
            textureCoordinates = gl_MultiTexCoord0.xy;
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
         }
 
      #endif
      #ifdef FRAGMENT 
         uniform vec4 _SinTime;
         varying vec2 textureCoordinates;
         void main() 
         {
            gl_FragColor = vec4(1.0,textureCoordinates.x,0.0,1.0);
         }
 
      #endif 
      ENDGLSL 
      }
   }
}