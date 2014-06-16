using UnityEngine;
using System.Collections;

public class rotate_me : MonoBehaviour 
{
	public Vector3 rotation = new Vector3(0,0,0);

	void Update () 
	{
		transform.Rotate(rotation * Time.deltaTime);
	}
}
