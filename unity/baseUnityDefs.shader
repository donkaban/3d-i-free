attribute vec4 gl_Vertex;         // position (in object coordinates, 
attribute vec4 gl_Color;          // color (usually constant)
attribute vec3 gl_Normal;         // surface normal vector 
attribute vec4 gl_MultiTexCoord0; //0th set of texture coordinates 
attribute vec4 gl_MultiTexCoord1; //1st set of texture coordinates 



#ifndef UNITY_CG_INCLUDED
#define UNITY_CG_INCLUDED

// -------------------------------------------------------------------
// Common functions

float saturate(float x) 
{ 
	return max(0.0, min(1.0, x)); 
}


// -------------------------------------------------------------------
//  builtin values exposed from Unity

// Time values from Unity
uniform vec4 _Time;
uniform vec4 _SinTime;
uniform vec4 _CosTime;

// x = 1 or -1 (-1 if projection is flipped)
// y = near plane
// z = far plane
// w = 1/far plane
uniform vec4 _ProjectionParams;

// x = width
// y = height
// z = 1 + 1.0/width
// w = 1 + 1.0/height
uniform vec4 _ScreenParams;

// w = 1 / uniform scale
uniform vec4 unity_Scale;

uniform vec3 _WorldSpaceCameraPos;
uniform vec4 _WorldSpaceLightPos0;

uniform mat4 _Object2World, _World2Object;

uniform vec4 _LightPositionRange; // xyz = pos, w = 1/range

// -------------------------------------------------------------------
//  helper functions and macros used in many standard shaders

#if defined DIRECTIONAL || defined DIRECTIONAL_COOKIE
#define USING_DIRECTIONAL_LIGHT
#endif

#if defined DIRECTIONAL || defined DIRECTIONAL_COOKIE || defined POINT || defined SPOT || defined POINT_NOATT || defined POINT_COOKIE
#define USING_LIGHT_MULTI_COMPILE
#endif


#ifdef VERTEX

// Computes world space light direction
vec3 WorldSpaceLightDir( vec4 v )
{
	vec3 worldPos = (_Object2World * v).xyz;
	#ifndef USING_LIGHT_MULTI_COMPILE
		return _WorldSpaceLightPos0.xyz - worldPos * _WorldSpaceLightPos0.w;
	#else
		#ifndef USING_DIRECTIONAL_LIGHT
		return _WorldSpaceLightPos0.xyz - worldPos;
		#else
		return _WorldSpaceLightPos0.xyz;
		#endif
	#endif
}

// Computes object space light direction
vec3 ObjSpaceLightDir( vec4 v )
{
	vec3 objSpaceLightPos = (_World2Object * _WorldSpaceLightPos0).xyz;
	#ifndef USING_LIGHT_MULTI_COMPILE
		return objSpaceLightPos.xyz - v.xyz * _WorldSpaceLightPos0.w;
	#else
		#ifndef USING_DIRECTIONAL_LIGHT
		return objSpaceLightPos.xyz - v.xyz;
		#else
		return objSpaceLightPos.xyz;
		#endif
	#endif
}

// Computes world space view direction
vec3 WorldSpaceViewDir( vec4 v )
{
	return _WorldSpaceCameraPos.xyz - (_Object2World * v).xyz;
}

// Computes object space view direction
vec3 ObjSpaceViewDir( vec4 v )
{
	vec3 objSpaceCameraPos = (_World2Object * vec4(_WorldSpaceCameraPos.xyz, 1.0)).xyz * unity_Scale.w;
	return objSpaceCameraPos - v.xyz;
}

// Declares 3x3 matrix 'rotation', filled with tangent space basis
#define TANGENT_SPACE_ROTATION \
	vec3 binormal = cross( gl_Normal.xyz, Tangent.xyz ) * Tangent.w; \
	mat3 rotation = mat3( \
			Tangent.x, binormal.x, gl_Normal.x, \
			Tangent.y, binormal.y, gl_Normal.y, \
			Tangent.z, binormal.z, gl_Normal.z );


// Transforms float2 UV by scale/bias property (new method)
#define TRANSFORM_TEX(tex,name) (tex.xy * name##_ST.xy + name##_ST.zw)
// Transforms float4 UV by a texture matrix (old method)
#define TRANSFORM_UV(idx) (gl_TextureMatrix[idx] * gl_TexCoord[0] ).xy

#endif



// Calculates UV offset for parallax bump mapping
vec2 ParallaxOffset( float h, float height, vec3 viewDir )
{
	h = h * height - height/2.0;
	vec3 v = normalize(viewDir);
	v.z += 0.42;
	return h * (v.xy / v.z);
}


// Converts color to luminance (grayscale)
float Luminance( vec3 c )
{
	return dot( c, vec3(0.22, 0.707, 0.071) );
}


#endif // VERTEX
