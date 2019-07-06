import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LekComponent } from './lek.component';

describe('LekComponent', () => {
  let component: LekComponent;
  let fixture: ComponentFixture<LekComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LekComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LekComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
