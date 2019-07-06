import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewMyLocationsComponent } from './view-my-locations.component';

describe('ViewMyLocationsComponent', () => {
  let component: ViewMyLocationsComponent;
  let fixture: ComponentFixture<ViewMyLocationsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewMyLocationsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewMyLocationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
