#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
int gSL=0;
typedef struct node{
  int val;
  struct node * next;
} node_t;
void swap(void *vp1, void *vp2, int elemSize){
  char buffer[elemSize];
  memcpy(buffer, vp1, elemSize);
  memcpy(vp1, vp2, elemSize);
  memcpy(vp2, buffer, elemSize);
}
void insort(void *array, int sz, int elemSize, int (*cmp)(void *, void *)){
  char *start = array;
  char *end = array + sz*elemSize;
  char *i;
  for(i = start+elemSize; i<end; i=i+elemSize){
    char *previous = i;
    char *current = previous-elemSize;
    while(current>=start && cmp(previous, current)<0){
      swap(previous, current, elemSize);
      previous=current;
      current=current-elemSize;
    }
  }
}
int cmpInt(void *vp1, void *vp2){
  int a = *(int *)vp1;
  int b = *(int *)vp2;
  return (a>b) - (a<b);
}
int cmpFloat(void *vp1, void *vp2){
  float a = *(int *)vp1;
  float b = *(int *)vp2;
  return (a>b) - (a<b);    
}
int cmpStr(void *vp1, void *vp2){
  char *a = *(char **)vp1;
  char *b = *(char **)vp2;
  int max;
  if(strlen(a)<strlen(b)){
    max=strlen(b);
  }
  else{
    max=strlen(a);
  }
  int j;
  for(j=0; j<max; j++){
    if(a[j]!=b[j]){
      return (a[j]>b[j])-(a[j]<b[j]);
    }
  }
  return 0;
}
int cmpArr(void *vp1, void *vp2){
  int sum1=0;
  int sum2=0;
  int j;
  for(j=0; j<6; j++){
    sum1=sum1+((int *)vp1)[j];
    sum2=sum2+((int *)vp2)[j];
  }
  return (sum1<sum2)-(sum1>sum2);
}
int findMax(node_t * head){
  node_t * c= head;
  int maxnode = 0;
  if(c!=NULL){
    maxnode = c->val;
  }
  while(c!=NULL){
    //printf("%x, %x\n", c->val, maxnode);
    if((c->val)>maxnode){
      maxnode = c->val;
    }
    c=c->next;
  }
  //printf("One linked list done.\n");
  return maxnode;
}
int cmpNode(void *vp1, void *vp2){
  node_t *a = *(node_t **)vp1;
  node_t *b = *(node_t **)vp2;
  int maxa = findMax(a);
  int maxb = findMax(b);
  return (maxa<maxb)-(maxa>maxb);
}
int main(){
  int a1[] = {35, 4, 5, 2, 78, 16, 5, 1};
  float a2[] = {-2.5f, 4.1f, 5.2f, 2.3f, 7.8f, 16.0f, 5.2f, 1.9f};
  char *a3[] = {"Apples","Pears", "Bananas", "Guavas"};
  int a4[][6] = {{1,8,9,10,2,3},{7,0,5,12,4,1}};
  gSL=6;
  node_t * h = malloc(sizeof(node_t));
  h->val = 1;
  node_t * g = malloc(sizeof(node_t));
  g->val = 3;
  g->next = NULL;
  h->next = g;
  node_t * x = malloc(sizeof(node_t));
  node_t * y = malloc(sizeof(node_t));
  x->val = 2;
  node_t * z = malloc(sizeof(node_t));
  x->next = y;
  y->val = 5;
  y->next = z;
  z->val = 0;
  node_t * w = malloc(sizeof(node_t));
  w->val = 4;
  w->next = NULL;
  node_t * a5[] = {h, x, w};
  insort(&a5, 3, sizeof(node_t *), cmpNode);
  int i = 0;
  for(i = 0; i<3; i++){
    node_t * current = a5[i];
    while(current!=NULL){
      printf("%d,", current->val);
      current = current->next;
    }
    printf("\n");
  }
}  
