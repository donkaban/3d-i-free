using UnityEngine;
using System.Collections;
 
public class mouse_rotate : MonoBehaviour 
{
  
    public float sensitivityX = 5.0f;
    public float sensitivityY = 5.0f;
    private Transform cameraTm;
    private bool down = false;

    void Start ()
    {
        cameraTm = Camera.mainCamera.transform;
    }
  
    void Update () 
    {
        float rotationX = Input.GetAxis("Mouse X") * sensitivityX;
        float rotationY = Input.GetAxis("Mouse Y") * sensitivityY;
        transform.RotateAroundLocal( cameraTm.up, -Mathf.Deg2Rad * rotationX );
        transform.RotateAroundLocal( cameraTm.right, Mathf.Deg2Rad * rotationY );
    }
}